from Bio import Entrez
from Bio import SeqIO

# Put your email here
Entrez.email = "jbpinzer@wpi.edu"

protein_ids = input("Put in some protein IDs, separate with spaces: ")

# Collect data of each protein
handle = Entrez.efetch(db="nucleotide",
                       id=protein_ids.split(),
                       rettype="fasta")

# Use SeqIO to parse all the protein data
records = list(SeqIO.parse(handle, "fasta"))

# Initialize vars
shortest_id = 0
shortest_length = len(records[0].seq)
count = 0

# Go through all the records to find the shortest length FASTA and which index in the list of ids it is.
for x in records:
    if shortest_length > len(x.seq):
        shortest_length = len(x.seq)
        shortest_id = count
    count += 1

print(">" + records[shortest_id].description)
print(records[shortest_id].seq)
