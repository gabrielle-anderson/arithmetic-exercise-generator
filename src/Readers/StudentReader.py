import os

import openpyxl

from src.Misc.auxiliary import cellValues
from src.ProblemSpecifications.StudentSpecification import StudentSpecification


class StudentReader:
    def __init__(self):
        self.requiredSheetNames = ["Students"]
        self.requiredFirstLevelHeaders = ["Student", None, "Addition", None, "Subtraction", None, "Multiplication", None, "Division", None]
        self.requiredSecondLevelHeaders =  ["Name", "Group", "Problem level", "No of problems", "Problem level", "No of problems", "Problem level", \
             "No of problems", "Problem level", "No of problems"]
        self.workbook = None

    def getStudents(self, path):
        self.workbook = openpyxl.load_workbook(path)
        assert (self.workbook.get_sheet_names() == self.requiredSheetNames), \
            "Worksheet names should be %s and instead are %s." % (
            self.requiredSheetNames, self.workbook.get_sheet_names())

        sheet = self.workbook.get_sheet_by_name("Students")

        firstLevelHeaders = cellValues(sheet.rows[0])
        secondLevelHeaders = cellValues(sheet.rows[1])

        assert (self.requiredFirstLevelHeaders == firstLevelHeaders), \
            "First row names should be %s and instead are %s." % (
                self.requiredFirstLevelHeaders, firstLevelHeaders)
        assert (self.requiredSecondLevelHeaders == secondLevelHeaders), \
            "Second row names should be %s and instead are %s." % (
                self.requiredSecondLevelHeaders, secondLevelHeaders)

        result = {}
        for row in sheet.iter_rows(row_offset=2):
            values = cellValues(row)
            if (len(values) == len(self.requiredFirstLevelHeaders) and values[0] != None):
                specification = StudentSpecification(values[1], values[2], values[3], values[4], values[5], values[6], \
                                                         values[7], values[8], values[9])
                result[values[0]] = specification
        return result


# os.chdir(os.pardir + "/" + os.pardir + "/specifications")
# fileName = "studentInfo.xlsx"
#
# reader = StudentReader()
# reader.getStudents(fileName)