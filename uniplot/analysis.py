from functools import reduce


def add(x, y):
    """Add two numbers together"""
    return x + y


def average_len(records):
    """Return the average len for records."""
    record_total = len(records)

    sequence_lengths = []
    for record in records:
        sequence = len(record)
        sequence_lengths.append(sequence)
        sequence_total = reduce(add, sequence_lengths)

    return sequence_total/record_total


def average_len_taxa(records, depth):
    """Return the average length for the top level taxa"""
    record_by_taxa = {}
    for r in records:
        taxa = r.annotations["taxonomy"][depth]
        record_by_taxa.setdefault(taxa, []).append(r)

    return {taxa: average_len(record) for (taxa, record) in record_by_taxa.items()}
