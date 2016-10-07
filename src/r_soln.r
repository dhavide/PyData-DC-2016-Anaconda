# -*- coding: utf-8 -*-
to_fahrenheit <- function(t_celcius) {
    # Transforms temperature from Celcius (°C) to Fahrenheit (°F)
    t_fahrenheit <- 1.8 * t_celcius + 32.0
    return(t_fahrenheit)
}

n_header = 25 # Keep line 26 for column labels
my_data = read.table('../data/eng-daily-01012015-12312015.csv',
                      header=TRUE, skip=n_header, sep=',', row.names=1)

# Construct format string with Unicode symbols embedded
deg_sym <- "\xC2\xB0"
num_fmt = sprintf("%%4.1f%sC/%%.1f%sF", deg_sym, deg_sym)
fmt = sprintf("Date: %%s\tMin.: %s\tMax.: %s\n", num_fmt, num_fmt)

nrows = nrow(my_data)
for(k in 1:nrows) {
    date <- rownames(my_data[k,])
    min_C <- my_data[k,7]
    max_C <- my_data[k,5]
    if (is.na(min_C) | is.na(max_C)) {
        cat('Missing data\n')
    } else {
    min_F <- to_fahrenheit(min_C)
        max_F <- to_fahrenheit(max_C)
        cat(sprintf(fmt, date, min_C, min_F, max_C, max_F))
    }
}
