from . import parse
from . import cli
from functools import reduce

def add(x,y):
    return x + y

def sequence_total(loc):
    sequence_lengths = []
    for record in parse.uniprot_seqrecords(loc):
        sequence = len(record)
        sequence_lengths.append(sequence)
    return reduce(add,sequence_lengths)

def average_len(records):
    """Returns the average len for records."""
    record_total = len(records)
    return sequence_total(cli.loc())/record_total

