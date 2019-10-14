import gzip
from Bio import SeqIO

#for l in gzip.open("uniprot_receptor.xml.gz"):
    #print(l.decode('utf-8').strip())


def cli():
    handle = gzip.open("uniprot_receptor.xml.gz")
    for record in SeqIO.parse(handle, "uniprot-xml"):
        print(record)
