# coding: utf-8

from __future__ import print_function
import pytest
import os
import docutils.core

def find_test_vectors():
    basedir = os.path.join(os.path.dirname(__file__), "vectors")
    return [os.path.join(basedir, name) for name in os.listdir(basedir)]


@pytest.mark.parametrize("inputfile", find_test_vectors())
def test_vector(inputfile):
    """
    Parse test vector (an reST file) and check that reparsing the writers
    output results in the same doctree.
    """
    source = open(inputfile, "rb").read()
    recreated_source = docutils.core.publish_string(source, writer_name="docutils_rest_writer.Writer")
    print(recreated_source)
    assert docutils.core.publish_string(source) == docutils.core.publish_string(recreated_source)
