#!/usr/bin/env python

"""
A minimal front end to the Docutils Publisher, reproducing reStructuredText
from the reStructuredText input.
"""

def rst2rst():
    try:
        import locale
        locale.setlocale(locale.LC_ALL, '')
    except:
        pass

    from docutils.core import publish_cmdline, default_description

    description = ('Recreates a reStructuredText representation from '
            'reStructuredText sources.  ' + default_description)

    publish_cmdline(writer_name='docutils_rest_writer.Writer',
            description=description)
