import openpyxl

class SpecificationReader:
    requiredSheetNames = ["Operand 1", "Operand 2", "Explicit number ranges", "Adjusting", "Misc"]
    def __init__(self, path):
        self.workbook = openpyxl.load_workbook(path)
        print path
        print self.workbook
        assert (self.workbook.get_sheet_names() == self.requiredSheetNames), \
            "Worksheet names should be %s and instead are %s." % (self.requiredSheetNames, self.workbook.get_sheet_names())
