from Bio import Entrez
Entrez.email = "jbpinzer@wpi.edu"
name = input("Genus to search: ")
start_date = input("Start Date (YYYY/MM/DD): ")
end_date = input("End Date (YYYY/MM/DD): ")

handle = Entrez.esearch("nucleotide", '"{}"[Organism] AND ("{}"[PDAT] : "{}"[PDAT])'.format(name, start_date, end_date))
record = Entrez.read(handle)

print("Counted {} items".format(record["Count"]))
