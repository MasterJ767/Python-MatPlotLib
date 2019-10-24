import os


def find():
    """Find uniprot xml file"""
    if os.path.exists('uniprot_receptor.xml.gz') == True:
        file = os.path.abspath('uniprot_receptor.xml.gz')
        return os.path.relpath(file, '/uniplot/cli.py')
