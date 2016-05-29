# -*- coding: UTF-8 -*-
from budget_app.models import *
from budget_app.loaders import SimpleBudgetLoader
from decimal import *
import csv
import os
import re

class SantiagoBudgetLoader(SimpleBudgetLoader):

    # An artifact of the in2csv conversion of the original XLS files is a trailing '.0', which we remove here
    def clean(self, s):
        return s.split('.')[0]

    def parse_item(self, filename, line):
        # Programme codes have changed in 2015, due to new laws. Since the application expects a code-programme
        # mapping to be constant over time, we are forced to amend budget data prior to 2015.
        # See https://github.com/dcabo/presupuestos-aragon/wiki/La-clasificaci%C3%B3n-funcional-en-las-Entidades-Locales
        programme_mapping = {
            # old programme: new programme
            '13400': '13500',
            '13500': '13600',
            '15200': '15220',
            '15500': '15320',
            '23000': '23100',
            '23102': '23109',
            '23200': '23102',
            '23201': '23103',
            '23202': '23104',
            '23203': '23100',
            '23300': '23100',
            '31300': '31100',
            '32100': '32300',
            '32101': '32301',
            '32102': '32302',
            '32200': '32400',
            '32300': '32600',
            '32400': '32600',
            '33201': '33220',
            '33601': '33600',
            '43101': '43120',
            '44100': '44110',

        }

        is_expense = (filename.find('gastos.csv')!=-1)
        is_actual = (filename.find('/ejecucion_')!=-1)
        if is_expense:
            # We got 5-digit functional codes as input, but leading zero may be lost
            fc_code = line[1].rjust(5, '0')

            # For years before 2015 we check whether we need to amend the programme code
            year = re.search('municipio/(\d+)/', filename).group(1)
            if int(year) < 2015:
                fc_code = programme_mapping.get(fc_code, fc_code)

            # Institutional codes are 3-digits (although leading zeros tend to disappear).
            # But in order to fit with our data model we need to treat them as department codes,
            # adding two leading zeros for institution and section.
            # Slightly more complicated: codes are inconsistent across years, so we're going
            # to use separate code tables for each year: we append the year's last two digits.
            ic_code = line[0].rjust(5, '0')+'-'+year[-2:]

            return {
                'is_expense': True,
                'is_actual': is_actual,
                'fc_code': fc_code,
                'ec_code': line[2][:-2],        # First three digits (everything but last two)
                'ic_code': ic_code,
                'item_number': line[2][-2:],    # Last two digits
                'description': line[3],
                'amount': self._parse_amount(line[10 if is_actual else 7])
            }

        else:
            return {
                'is_expense': False,
                'is_actual': is_actual,
                'ec_code': line[0][:-2],        # First three digits (everything but last two)
                'ic_code': '00000',             # All income goes to the root node
                'item_number': line[0][-2:],    # Last two digits
                'description': line[1],
                'amount': self._parse_amount(line[5 if is_actual else 2])
            }
