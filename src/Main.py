import os
import glob
import re

from SpecificationReader import SpecificationReader

os.chdir(os.pardir + "/specifications/multiplication")
print os.getcwd()
p = re.compile("\d+.xlsx")
for file in glob.glob("*.xlsx"):
    if (p.match(file)):
        # print(file)
        sr = SpecificationReader(file)