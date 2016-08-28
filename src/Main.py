import datetime
import glob
import re

from StudentReader import StudentReader

from ProblemSheetWriter import ProblemSheetWriter
from SpecificationReader import *
from constants import *


def processSpecifications(parameters):
    result = {}
    os.chdir(os.curdir + parameters.directory)
    # print os.getcwd()
    integerNamePattern = re.compile("\d+")
    files = glob.glob("*.xlsx")
    files = [os.path.splitext(file)[0] for file in files]
    files = filter(lambda file: integerNamePattern.match(file), files)
    files = [int(file) for file in files]
    for file in sorted(files):
        fileName = str(file) + ".xlsx"
        specificationReader = SpecificationReader()
        problemSpecification = specificationReader.getProblem(fileName, parameters.operation, parameters.constructor)
        # (o1, o2) = problemSpecification.randomOperands()
        result[file] = problemSpecification
        # print str(o1) + " " + str(o2) + "\n\n"
    return result

start =  datetime.datetime.now()
rootDir = os.path.dirname(os.getcwd())

os.chdir(os.pardir + os.sep + "specifications")

additionProblems = processSpecifications(plus)
os.chdir(os.pardir)
subtractionProblems = processSpecifications(minus)
os.chdir(os.pardir)
multiplicationProblems = processSpecifications(times)
os.chdir(os.pardir)
divisionProblems = processSpecifications(divides)
os.chdir(os.pardir)


os.chdir(rootDir + os.sep + "specifications")
fileName = "studentInfo.xlsx"
students = StudentReader().getStudents(fileName)

for studentName in students.keys():
    os.chdir(rootDir + os.sep + "Problem sheets")
    studentSpecification = students[studentName]
    # print str(studentName) + " " + str(students[studentName])
    ProblemSheetWriter().writeStudentProblems(studentName, studentSpecification, additionProblems, subtractionProblems, \
                         multiplicationProblems, divisionProblems)


end = datetime.datetime.now()

# print end - start