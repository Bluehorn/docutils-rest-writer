# coding: utf-8

import re
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
        self._stack = []

    def astext(self):
        return "".join(self.body)

    def visit_document(self, node):
        pass

    def depart_document(self, node):
        pass

    def visit_title(self, node):
        self._stack.append(("title", self.body))
        self.body = []

    def depart_title(self, node):
        title_body = "".join(self.body)
        tag, self.body = self._stack.pop()
        assert tag == "title"
        self.body.append(title_body + "\n")
        self.body.append("=" * len(title_body) + "\n\n")

    def visit_block_quote(self, node):
        self._stack.append(("block_quote", self.body))
        self.body = []

    def depart_block_quote(self, node):
        quoted = ["    %s\n" % (l,) for l in "".join(self.body).splitlines()]
        tag, self.body = self._stack.pop()
        assert tag == "block_quote"
        self.body.append("".join(quoted))

    def visit_emphasis(self, node):
        self.body.append("*")

    def depart_emphasis(self, node):
        self.body.append("*")

    def visit_strong(self, node):
        self.body.append("**")

    def depart_strong(self, node):
        self.body.append("**")

    def visit_literal(self, node):
        self.body.append("``")

    def depart_literal(self, node):
        self.body.append("``")

    def visit_section(self, node):
        pass

    def depart_section(self, node):
        pass

    def visit_paragraph(self, node):
        pass

    def depart_paragraph(self, node):
        self.body.append("\n\n")

    def visit_Text(self, node):
        escaped_text = re.sub(r'[*]', lambda match: {"*": "\\*"}[match.group()], node.astext())
        self.body.append(escaped_text)

    def depart_Text(self, node):
        pass
