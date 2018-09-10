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
        payee = re.sub('\s\s+', ' ', payee)
        payee = self._titlecase(payee)
        payee = re.sub(r' A ', ' a ', payee)
        payee = re.sub(r' E ', ' e ', payee)
        payee = re.sub(r' I ', ' i ', payee)
        payee = re.sub(r' Y ', ' y ', payee)
        payee = re.sub(r' O ', ' o ', payee)
        payee = re.sub(r' D\'', ' d\'', payee)
        payee = re.sub(r' De ', ' de ', payee)
        payee = re.sub(r' Del ', ' del ', payee)
        payee = re.sub(r' La ', ' la ', payee)
        payee = re.sub(r' Lo ', ' lo ', payee)
        payee = re.sub(r' Da ', ' da ', payee)
        payee = re.sub(r' Do ', ' do ', payee)
        payee = re.sub(r' En ', ' en ', payee)
        payee = re.sub(r'^Ncg ', 'NCG ', payee)
        payee = re.sub(r'^Ute ', 'UTE ', payee)
        payee = re.sub(r'^Iss ', 'ISS ', payee)
        payee = re.sub(r'^Hpc ', 'HPC ', payee)
        payee = re.sub(r'^Cps ', 'CPS ', payee)
        payee = re.sub(r'^Cys ', 'CYS ', payee)
        payee = re.sub(r'^Api ', 'API ', payee)
        payee = re.sub(r'^Ac ', 'AC ', payee)
        payee = re.sub(r'^Tdn ', 'TDN ', payee)
        payee = re.sub(r'^Apa ', 'APA ', payee)
        payee = re.sub(r'^Iec ', 'IEC ', payee)
        payee = re.sub(r'^Ies ', 'IES ', payee)
        payee = re.sub(r'^Ceip ', 'CEIP ', payee)
        payee = re.sub(r'^Vsm ', 'VSM ', payee)
        payee = re.sub(r'^10D10 ', '10d10 ', payee)
        payee = re.sub(r'^Yago\'S ', 'Yago\'s ', payee)
        payee = re.sub(r'^Fh ', 'FH ', payee)
        payee = re.sub(r'^Al Air Liquide ', 'AL Air Liquide ', payee)
        payee = re.sub(r' Cp', ' CP ', payee)
        payee = re.sub(r' Sdg ', ' SDG ', payee)
        payee = re.sub(r' Sa$', ' SA', payee)
        payee = re.sub(r' Sau$', ' SAU', payee)
        payee = re.sub(r' Sl$', ' SL', payee)
        payee = re.sub(r' Sl Ne$', ' SL NE', payee)
        payee = re.sub(r' Sll$', ' SLL', payee)
        payee = re.sub(r' Slu$', ' SLU', payee)
        payee = re.sub(r' Sc$', ' SC', payee)
        payee = re.sub(r',Sc$', ' SC', payee)
        payee = re.sub(r' Sae$', ' SAE', payee)
        payee = re.sub(r' Slp$', ' SLP', payee)
        payee = re.sub(r' Ute$', ' UTE', payee)
        payee = re.sub(r' Cb$', ' CB', payee)
        payee = re.sub(r' Scp$', ' SCP', payee)
        payee = re.sub(r' Cf$', ' CF', payee)
        payee = re.sub(r' Sc Galega$', ' SC Galega', payee)
        payee = re.sub(r' Lugo Sa ', ' Lugo SA ', payee)
        payee = re.sub(r' Servicios Sa ', ' Servicios SA ', payee)
        payee = re.sub(r' Sociosanitarios Sa ', ' Sociosanitarios SA ', payee)
        payee = re.sub(r' Transportes Sa ', ' Transportes SA ', payee)
        payee = re.sub(r' Barca Ma ', ' Barca MA ', payee)
        payee = re.sub(r'^Us Eventos ', 'US Eventos ', payee)
        payee = re.sub(r'^Dst Software ', 'DST Software ', payee)
        payee = re.sub(r' Xii ', ' XII ', payee)
        payee = re.sub(r' Xxi ', ' XXI ', payee)
        payee = re.sub(r' Xxiii ', ' XXIII ', payee)
        payee = re.sub(r' Clc ', ' CLC ', payee)
        payee = re.sub(r' Cnc ', ' CNC ', payee)
        payee = re.sub(r' Tv ', ' TV ', payee)
        payee = re.sub(r'^Singulae P & C', 'Singulae P&C', payee)
        payee = re.sub(ur'"" a Traiña""', u'"A Traiña"', payee)
        payee = re.sub(r' Sl Fs ', ' SL FS ', payee)
        payee = re.sub(r'^Empresa Gasoleo de Calefaccion ', u'Gasoleo Calefacción ', payee)
        payee = re.sub(r' Calefaccion ', u' Calefacción ', payee)
        payee = re.sub(r'^Cluster Tic ', 'Cluster TIC ', payee)

        payee_id = line[9].strip()
        payee = ("Anonimizado" if payee_id == "Anonimizado" else payee)

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
            'ic_code': None,
            'date': date,
            'payee': payee,
            'anonymized': anonymized,
            'description': description,
            'amount': amount
        }
