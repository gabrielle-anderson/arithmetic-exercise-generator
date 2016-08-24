from types import *
from Bounds import Bounds
from Operand import Operand


class OperandSpecification:
    def __init__(self):
        self.digits = {}
        self.explicitRange = []

    def addDigit(self, unit, lowerBound, upperBound):
        # assert type(unit) is FloatType, "unit is not a float" + str(unit)
        self.digits[unit] = Bounds(lowerBound, upperBound)

    def setExplicitRange(self, explicitRange):
        self.explicitRange = explicitRange

    def __str__(self):
        result = ""
        for digit in self.digits.keys():
            result += "U: " + str(digit) + " " + str(self.digits[digit]) + "\n"
        return result

    def randomOperand(self):
        operand = Operand()
        for digit in self.digits.keys():
            operand.addDigit(digit, self.digits[digit].randomInt())
        if (self.explicitRange == []):
            return operand
        elif (self.explicitRange != [] and operand.value() in self.explicitRange):
            return operand
        else:
            return self.randomOperand()