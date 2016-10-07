# -*- coding: utf-8 -*-
def to_fahrenheit(t_celcius):
    u'Transforms temperature from Celcius (°C) to Fahrenheit (°F)'
    t_fahrenheit = 1.8 * t_celcius + 32.0
    return t_fahrenheit

with open('../data/eng-daily-01012015-12312015.csv', 'r') as f:
    n_header = 26 # Skip over all lines in the file header
    for k in range(n_header):
        f.readline()

    # Construct format string with Unicode symbols embedded
    deg_sym = u'\N{degree sign}'
    num_fmt = u'%%4.1f%sC/%%.1f%sF' % ((deg_sym,) * 2)
    fmt = u'Date: %%s\tMin.: %s\tMax.: %s' % ((num_fmt,) * 2)

    for line in f:
        try:
            fields = line.strip().replace('"', '').split(',')
            date, max_C, min_C = (
                         fields[0], float(fields[5]), float(fields[7]))
            min_F, max_F = map(to_fahrenheit, [min_C, max_C])
            print fmt % (date, min_C, min_F, max_C, max_F)
        except ValueError:
            print 'Missing data'
