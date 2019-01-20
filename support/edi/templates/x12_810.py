# Invoice
# Based on X12 004010 V1 Variant 10

from . import generic, template_operators
import io


desc = "Invoice"
i = 810

class Template(generic.Template):
    def __init__(self, edi_file: io.BytesIO):
        self._edi_file = edi_file
        generic.Template.__init__(self, self._edi_file, i, desc)


class TemplateDescription(generic.TemplateDescription):
    def __init__(self):
        generic.TemplateDescription.__init__(self, i, desc, Template)


description = TemplateDescription()