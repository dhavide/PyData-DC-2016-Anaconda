# -*- coding: utf-8 -*-
import pandas as pd

# Read csv file directly into a pandas dataframe
n_header = 25 # Keep row 26 for column names
my_data = pd.read_csv('../data/eng-daily-01012015-12312015.csv',
                      skiprows=n_header, encoding='utf-8', index_col=0)

# Redefine data frame with desired columns only
my_data = my_data[[u'Min Temp (°C)', u'Max Temp (°C)']]
def to_fahrenheit(t_celcius):
    'Transforms temperature from Celcius (°C) to Fahrenheit (°F)'
    t_fahrenheit = 1.8 * t_celcius + 32.0
    return t_fahrenheit
my_data[u'Min Temp (°F)'] = to_fahrenheit(my_data[u'Min Temp (°C)'])
my_data[u'Max Temp (°F)'] = to_fahrenheit(my_data[u'Max Temp (°C)'])

# Construct format string with Unicode symbols embedded
deg_sym = u'\N{degree sign}'
num_fmt = u'%%4.1f%sC/%%.1f%sF' % ((deg_sym,) * 2)
fmt = u'Date: %%s\tMin.: %s\tMax.: %s' % ((num_fmt,) * 2)

for date in my_data.index:
    min_C, max_C, min_F, max_F = my_data.loc[date,:]
    print fmt % (date, min_C, min_F, max_C, max_F)
