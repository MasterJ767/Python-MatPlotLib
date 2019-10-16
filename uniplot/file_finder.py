import os

def find():
    if os.path.exists('uniprot_receptor.xml.gz') == True:
        file = os.path.abspath('uniprot_receptor.xml.gz')
        return os.path.relpath(file, '/uniprot/cli.py')
