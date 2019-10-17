import argparse
from . import parse
from . import analysis
from . import plot
from . import file_finder

loc = file_finder.find()


def dump(args):
    """Print the entire contents of the file."""
    for record in parse.uniprot_seqrecords(loc):
        print(record)


def names(args):
    """Print the name of each record."""
    for record in parse.uniprot_seqrecords(loc):
        print(record.name)


def average(args):
    """Print the average len for records."""
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(loc))))


def plot_average_by_taxa(args):
    """Display bar chart with average len per taxa"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(loc), )
    plot.plot_bar_show(av)


def cli():
    """Add parsing capabilities to the cli"""
    # Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    # Add subparsers
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("plot").add_argument("--depth",,type=int,default=0).set_defaults(func=plot_average_by_taxa)

    # Parse the command line
    args = parser.parse_args()

    # Take the func argument, which points to our function and call it.
    args.func(args)
