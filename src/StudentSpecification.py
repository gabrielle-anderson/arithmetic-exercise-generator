from constants import *


class StudentSpecification:
    def __init__(self, group, additionLevel, noAddition, subtractionLevel, noSubtraction, \
                 multiplicationLevel, noMultiplication, divisionLevel, noDivision):
        self.group = group
        self.additionLevel = additionLevel
        self.noAddition = noAddition
        self.subtractionLevel = subtractionLevel
        self.noSubtraction = noSubtraction
        self.multiplicationLevel = multiplicationLevel
        self.noMultiplication = noMultiplication
        self.divisionLevel = divisionLevel
        self.noDivision = noDivision

    def __str__(self):
        return "(" + str(self.group) + "): " + \
               str(self.noAddition) + " addition problems at level " + str(self.additionLevel) + ", " + \
               str(self.noSubtraction) + " subtraction problems at level " + str(self.subtractionLevel) + ", " + \
               str(self.noMultiplication) + " multiplication problems at level " + str(self.multiplicationLevel) + ", " + \
               str(self.noDivision) + " division problems at level " + str(self.divisionLevel)

    def toStringShort(self):
        return additionString + ":" + str(self.additionLevel) + ", " + \
               subtractionString + ":"  + str(self.subtractionLevel) + ", " +\
               multiplicationString +  ":" + str(self.multiplicationLevel) + ", " + \
               divisionString + ":" + str(self.divisionLevel)

    def getProblemLevel(self, problemName):
        if problemName == additionString:
            return self.additionLevel
        elif problemName == subtractionString:
            return self.subtractionLevel
        elif problemName == multiplicationString:
            return self.multiplicationLevel
        elif problemName == divisionString:
            return self.divisionLevel

    def toProblemList(self):
        result = []
        for i in range(0,self.noAddition):
            result.append(additionString)
        for i in range(0,self.noSubtraction):
            result.append(subtractionString)
        for i in range(0,self.noMultiplication):
            result.append(multiplicationString)
        for i in range(0,self.noDivision):
            result.append(divisionString)

        return result
