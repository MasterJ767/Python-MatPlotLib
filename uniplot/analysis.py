from . import parse

loc = "uniprot_receptor.xml.gz"

def average_len(records):
    # Returns the average len for records.
    for record in parse.uniprot_seqrecords(loc):
        return len(record)
