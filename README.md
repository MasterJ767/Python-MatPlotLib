CSC1034: Practical 2
====================

This package allows analysis and display of proteins from the 'uniprot_receptor.xml.gz' file.

Dependencies:
------------
See 'Pipfile' for more details. 

How to use:
-----------

Use the following commands in the terminal to make use of the program:

- `python uniplot.py dump` - This will return all information about all protein chains.

- `python uniplot.py names` - This will return the names of each protein chain.

- `python uniplot.py average` - This will return the average length of a protein chain.

- `python uniplot.py plot-bar` - This will display a bar chart which represents the average length of 
protein chains by the highest taxonomic rank. 

Using `python uniplot.py --help` or `python uniplot.py -h` will display the information above in the terminal.

Built With:
-----------
Pycharm - IDE

Pipenv - Dependency management

License:
--------
See 'LICENSE.md' for more details
