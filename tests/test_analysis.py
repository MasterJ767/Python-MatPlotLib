import uniplot.analysis
import uniplot.parse

test_uniprot = "./resources/uniprot_sprot_small.xml.gz"


def test_hello_world():
    assert True


def test_average():
    """Test the average length function from analysis.py"""
    assert uniplot.analysis.average_len(
        uniplot.parse.uniprot_seqrecords(test_uniprot)
    ) == 302.72222222222223

