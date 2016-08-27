from types import *

from ProblemSpecification import ProblemSpecification
from src.Misc.auxiliary import *


class DivisionSpecification(ProblemSpecification):
    def __init__(self, o1, o2, resultRange, op, adjustments, miscParameters):
        self.firstOperandSpecification = o1
        self.secondOperandSpecification = o2
        self.resultExplicitRange = resultRange
        self.operation = op
        self.adjustments = adjustments
        self.miscParameters = miscParameters

    def digitAdjustments(self, firstOperand, secondOperand):
        divisor = secondOperand.value()
        dividend = 0
        result = {}

        for digit in sorted(firstOperand.digits.keys(), reverse=True):
            dividend = dividend + firstOperand.digits[digit]
            remainder = dividend % divisor
            result[digit] = (remainder != 0)

            dividend = remainder * 10

        return result

    def randomOperands(self):
        (firstOperand, secondOperand) = ProblemSpecification.randomOperands(self)

        if ("Recurring decimal" in self.miscParameters.keys()):
            value = self.miscParameters["Recurring decimal"]
            if (type(value) is BooleanType and hasRecurringDecimal(secondOperand.value()) != value):
                return self.randomOperands()

        return (firstOperand, secondOperand)
