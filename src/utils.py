

def num_approx(n, precision=1):
    suffixes = [
        (1, ''),
        (1e3, 'K'),
        (1e6, 'M'),
        (1e9, 'B'),
        (1e12, 'T'),
    ]

    for divisor, suffix in suffixes:
        if n < (1000*divisor):
            n_format = f'{n/divisor:.{precision}f}'
            break

    ## Remove trailing zeros after the decimal point if precision is greater than 0
    if precision > 0:
        n_format = n_format.rstrip('0').rstrip('.')

    return n_format + suffix