# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

MAIN_ENTITY_LEVEL = 'municipio'
MAIN_ENTITY_NAME = 'Santiago'

BUDGET_LOADER = 'SantiagoBudgetLoader'
PAYMENTS_LOADER = 'SantiagoPaymentsLoader'

FEATURED_PROGRAMMES = ['16500', '13200', '33800', '24100', 'XX']

OVERVIEW_INCOME_NODES = [
                          {
                            'nodes': [['11', '113']],
                            'label.es': 'Impuesto a bienes inmuebles de naturaleza urbana',
                            'label.gl': 'Imposto sobre inmobiliario de natureza urbana'
                          },
                          '42', '45', '13',
                          {
                            'nodes': [['11', '115']],
                            'label.es': 'Impuesto sobre vehículos de tracción mecánica',
                            'label.gl': 'Imposto sobre vehículos a motor'
                          },
                          {
                            'nodes': [['30', '302']],
                            'label.es': 'Servicio de recogida de basuras',
                            'label.gl': 'Servizo de recollida de lixo'
                          },
                          {
                            'nodes': [['39', '391']],
                            'label.es': 'Multas',
                            'label.gl': 'Multas'
                          },
                        ]
OVERVIEW_EXPENSE_NODES = ['16', '13', '92', '01', '15', '33', '23', '17', '44', '34', '32']

# How aggresive should the Sankey diagram reorder the nodes. Default: 0.79 (Optional)
# Note: 0.5 usually leaves nodes ordered as defined. 0.95 sorts by size (decreasing).
OVERVIEW_RELAX_FACTOR = 0.35

# Show Payments section in menu & home options. Default: False.
SHOW_PAYMENTS           = True

# Show Tax Receipt section in menu & home options. Default: False.
SHOW_TAX_RECEIPT        = True

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
SHOW_COUNTIES_AND_TOWNS = False

# Show an extra tab with institutional breakdown. Default: True.
SHOW_INSTITUTIONAL_TAB  = True

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = False


# Show Subtotals panel in Overview. Default: False
# SHOW_OVERVIEW_SUBTOTALS = True

# Calculate budget indicators (True), or show/hide the ones hardcoded in HTML (False). Default: True.
# CALCULATE_BUDGET_INDICATORS = False

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
#SHOW_ACTUAL = True

# Include financial income/expenditures in overview and global policy breakdowns. Default: False.
INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = True

# Search in entity names. Default: True.
SEARCH_ENTITIES = False

# Supported languages. Default: ('es', 'Castellano')
LANGUAGES = (
  ('gl', 'Galego'),
  ('es', 'Castellano'),
)

# Facebook Aplication ID used in social_sharing temaplate. Default: ''
# In order to get the ID create an app in https://developers.facebook.com/
FACEBOOK_ID             = '111960449295842'

# Google Analytics ID. Default: ''
# In order to get the ID create a Google Analytics Acount in https://analytics.google.com/analytics/web/
ANALYTICS_ID            = 'UA-28946840-23'

# Setup Data Source Budget link
DATA_SOURCE_BUDGET      = 'http://www.santiagodecompostela.gal/casa_concello/transparencia.php?idn=.%2FInformacion_economica_e_financieira&lg=gal'

# Setup Data Source Population link
DATA_SOURCE_POPULATION  = 'http://www.ine.es/jaxiT3/Tabla.htm?t=2868&L=0'

# Setup Data Source Inflation link
DATA_SOURCE_INFLATION   = 'http://www.ine.es/jaxiT3/Tabla.htm?t=10019&L=0'

# Setup Main Entity Web Url
MAIN_ENTITY_WEB_URL     = 'http://www.santiagodecompostela.gal'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_LEGAL_URL   = 'http://www.santiagodecompostela.gal/avisolegal.php?lg=gal'

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
COOKIES_URL             = 'http://www.santiagodecompostela.gal/avisolegal.php?lg=gal'

# Allow overriding of default treemap color scheme
# COLOR_SCALE = [ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf' ]
