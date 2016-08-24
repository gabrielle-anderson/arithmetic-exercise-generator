import os
import glob
import re
from Operations import *
from SpecificationReader import *

os.chdir(os.pardir + "/specifications/multiplication")
print os.getcwd()
integerNamePattern = re.compile("\d+")
files = glob.glob("*.xlsx")
files = [os.path.splitext(file)[0] for file in files]
files = filter(lambda file: integerNamePattern.match(file), files)
files = [int(file) for file in files]
for file in sorted(files):
    # print(file)
    fileName = str(file) + ".xlsx"
    specificationReader = SpecificationReader()
    problemSpecification = specificationReader.getProblem(fileName, times)
    (o1, o2) = problemSpecification.randomOperands()
    print str(o1) + " " + str(o2) + "\n\n"