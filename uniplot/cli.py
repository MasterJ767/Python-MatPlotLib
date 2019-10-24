import argparse
from . import parse
from . import analysis
from . import plot
from . import file_finder

file_location = file_finder.find()


def dump(args):
    """Print the entire contents of the file."""
    for record in parse.uniprot_seqrecords(file_location):
        print(record)


def names(args):
    """Print the name of each record."""
    for record in parse.uniprot_seqrecords(file_location):
        print(record.name)


def average(args):
    """Print the average len for records."""
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(file_location))))


def plot_average_by_taxa_bar(args):
    """Display bar chart with average len per taxa"""
    depth = int(input("Enter a taxa depth (0 - 20): "))
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(file_location), depth)
    plot.plot_bar_show(av)


def cli():
    """Add parsing capabilities to the cli"""
    # Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help:")

    # Add subparsers
    subparsers.add_parser("dump", help="This will return all information about all protein chains.").set_defaults(
        func=dump)
    subparsers.add_parser("list", help="This will return the names of each protein chain.").set_defaults(
        func=names)
    subparsers.add_parser("average", help="This will return the average length of a protein chain.").set_defaults(
        func=average)
    subparsers.add_parser("plot-bar", help="This will display a bar chart which represents the average length of "
                                           "protein chains by the highest taxonomic rank.").set_defaults(
        func=plot_average_by_taxa_bar)

    # Parse the command line
    args = parser.parse_args()

    # Take the func argument, which points to our function and call it.
    args.func(args)
