# coding: utf-8

import docutils.writers
import docutils.nodes


class Writer(docutils.writers.Writer):

    supported = ('rest',)
    """Formats this writer supports."""

    config_section = 'rest writer'
    config_section_dependencies = ('writers',)

    def __init__(self):
        docutils.writers.Writer.__init__(self)
        self.translator_class = Translator

    def translate(self):
        visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.astext()


class Translator(docutils.nodes.NodeVisitor):

    def __init__(self, document):
        docutils.nodes.NodeVisitor.__init__(self, document)
        self.body = []

    def astext(self):
        return "".join(self.body)

    def visit_document(self, node):
        pass

    def depart_document(self, node):
        pass

    def visit_paragraph(self, node):
        pass

    def depart_paragraph(self, node):
        self.body.append("\n")

    def visit_Text(self, node):
        self.body.append(node.astext())

    def depart_Text(self, node):
        pass
