from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('A8B5P7')
record = SwissProt.read(handle)
processes = []
for x in record.cross_references:
    if x[0] == 'GO':
        if x[2][0] == 'P':
            processes.append(x[2])

for x in processes:
    print(x[2:])
