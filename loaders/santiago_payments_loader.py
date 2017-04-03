# -*- coding: UTF-8 -*-
import dateutil.parser
import re

from budget_app.loaders import PaymentsLoader
from budget_app.models import Budget

class SantiagoPaymentsLoader(PaymentsLoader):

    # Parse an input line into fields
    def parse_item(self, budget, line):

        policy_id = line[7].strip()[:2] # First two digits of the programme make the policy id
        # But what we want as area is the policy description
        policy = Budget.objects.get_all_descriptions(budget.entity)['functional'][policy_id]

        date = line[2].strip()
        date = dateutil.parser.parse(date, dayfirst=True).strftime("%Y-%m-%d")

        payee = line[10].strip()
        payee = ("Otros" if payee == "" else payee)
        payee = payee.replace(', ', ' ').replace(',', ' ')
        payee = re.sub('\s\s+', ' ', payee)
        payee = re.sub(r'CB$', 'C.B.', payee)
        payee = re.sub(r'SL$', 'S.L.', payee)
        payee = re.sub(r'S.L$', 'S.L.', payee)
        payee = re.sub(r'S.L$', 'S.L.', payee)
        payee = re.sub(r'S.L ', 'S.L. ', payee)
        payee = re.sub(r'SLL$', 'S.L.L.', payee)
        payee = re.sub(r'SLU$', 'S.L.U.', payee)
        payee = re.sub(r'SA$', 'S.A.', payee)
        payee = re.sub(r'SAU$', 'S.A.U.', payee)
        payee = re.sub(r'SC$', 'SDAD. COOP.', payee)
        payee = re.sub(r'SOC\. COOPERATIVA$', 'SDAD. COOP.', payee)
        payee = self._titlecase(payee)
        payee = re.sub(r' A ', ' a ', payee)
        payee = re.sub(r' E ', ' e ', payee)
        payee = re.sub(r' I ', ' i ', payee)
        payee = re.sub(r' Y ', ' y ', payee)
        payee = re.sub(r' D\'', ' d\'', payee)
        payee = re.sub(r' De ', ' de ', payee)
        payee = re.sub(r' Del ', ' del ', payee)
        payee = re.sub(r' La ', ' la ', payee)
        payee = re.sub(r' Lo ', ' lo ', payee)
        payee = re.sub(r' Da ', ' da ', payee)
        payee = re.sub(r' Do ', ' do ', payee)
        payee = re.sub(r'^Ncg ', 'NCG ', payee)
        payee = re.sub(r'^Ute ', 'UTE ', payee)
        payee = re.sub(r'^Iss ', 'ISS ', payee)
        payee = re.sub(r'^Hpc ', 'HPC ', payee)
        payee = re.sub(r'^Cps ', 'CPS ', payee)
        payee = re.sub(r' Sdg ', ' SDG ', payee)
        payee = re.sub(r'Lugo Sa', 'Lugo S.A.', payee)
        payee = re.sub(r'Servicios Sa', 'Servicios S.A.', payee)

        anonymized = False
        anonymized = (True if payee == "Anonimizado" else anonymized)

        description = line[11].strip()[:300]
        description = description.decode('utf-8','ignore').encode('utf-8')

        amount = line[3].strip()
        amount = self._read_english_number(amount)

        return {
            'area': policy,
            'programme': None,
            'fc_code': None,  # We don't try (yet) to have foreign keys to existing records
            'ec_code': None,
            'date': date,
            'contract_type': None,
            'payee': payee,
            'anonymized': anonymized,
            'description': description,
            'amount': amount
        }