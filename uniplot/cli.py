import argparse
from . import parse
from . import analysis

def loc():
    loc = "uniprot_receptor.xml.gz"
    #loc = "./resources/uniprot_sprot_small.xml.gz"
    return loc

def dump(args):
    """Prints the entire contents of the file."""
    for record in parse.uniprot_seqrecords(loc()):
        print(record)


def names(args):
    """Prints the name of each record."""
    for record in parse.uniprot_seqrecords(loc()):
        print(record.name)

def average(args):
    """Prints the average len for records."""
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(loc()))))


def cli():
    # Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    # Add subparsers
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)

    # Parse the command line
    args = parser.parse_args()

    # Take the func argument, which points to our function and call it.
    args.func(args)
