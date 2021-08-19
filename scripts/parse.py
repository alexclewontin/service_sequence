import os
import tabulate

basename = '/var/snap/seqtest/common/'

with open(os.path.join(basename, 'log.txt'), 'r') as f:
    raw = f.read()
    lines = raw.strip().split('\n')
    table = []
    for x in lines:
        idx, date = x.split(' ')
        date = float(date)
        table.append([idx, date])

    table = sorted(table, key=lambda x: x[1])
    print(tabulate.tabulate(table, floatfmt='.4f', tablefmt='plain'))

