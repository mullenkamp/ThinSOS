# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:50:00 2019

@author: michaelek
"""

from thinsos import SOS
import pandas as pd

pd.options.display.max_columns = 10

###################################
### Parameters

url = 'http://sensorweb.demo.52north.org/sensorwebtestbed/service'
url = 'https://climate-sos.niwa.co.nz'
token = ''

foi = '17244'
observed_property = 'MTHLY_STATS: TOTAL RAINFALL (MTHLY: TOTAL RAIN)'

foi = 'Vaisala-WXT520'
observed_property = 'WindSpeedAverage'

from_date = '2018-06-01'
to_date = '2018-10-01'

from_date = '2015-07-01'
to_date = '2015-08-01'

bbox = [[169.34, -45.3], [174.2, -41.7]]
bbox = [[0, 0], [60, 60]]

###################################
### Tests


sos1 = SOS(url, token)

json1 = sos1.get_capabilities()

#j1 = pd.read_json(json1)
#
#j2 = pd.DataFrame.from_dict(json1)

json2 = sos1.get_capabilities('all')


da1 = sos1.get_data_availability()
da1 = sos1.get_data_availability(foi=foi)

da2 = da1[da1.procedure == 'C'].copy()
da2.observedProperty.value_counts()

foi1 = sos1.get_foi()
#foi2 = sos1.get_foi(bbox=bbox)


obs1 = sos1.get_observation(foi, observed_property, from_date=from_date, to_date=to_date)

obs1.json()['observations']

body = sos1.filters(foi, procedure=None, observed_property=observed_property, from_date=from_date, to_date=to_date)

















