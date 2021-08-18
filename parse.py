import os
import tabulate

basename = '/var/snap/seqtest/common/'

for name in ['before', 'after']:
    with open(os.path.join(basename, f'{name}_log.txt'), 'r') as f:
        raw = f.read()
    lines = raw.strip().split('\n')
    table = []
    for x in lines:
        idx, date = x.split(' ')
        idx = int(idx)
        date = float(date)
        table.append([idx, date])

    table = sorted(table, key=lambda x: x[1])
    print(f'{name}:')
    print(tabulate.tabulate(table, floatfmt='.4f', tablefmt='plain'))

