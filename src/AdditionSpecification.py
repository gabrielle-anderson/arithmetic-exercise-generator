from ProblemSpecification import ProblemSpecification


class AdditionSpecification(ProblemSpecification):
    def __init__(self, o1, o2, resultRange, op, adjustments, miscParameters):
        assert (set(o2.digits.keys()) <= set(o1.digits.keys())), "First operand's set of digits must be a weak superset of the second's."
        self.firstOperandSpecification = o1
        self.secondOperandSpecification = o2
        self.resultExplicitRange = resultRange
        self.operation = op
        self.adjustments = adjustments
        self.miscParameters = miscParameters

    def digitAdjustments(self, firstOperand, secondOperand):
        result = {}
        carry = {}

        for digit in firstOperand.digits.keys():
            carry[digit] = 0
            carry[digit*10] = 0

        for digit in sorted(firstOperand.digits.keys()):
            if digit in secondOperand.digits.keys():
                resultOperation = self.operation(firstOperand.digits[digit], secondOperand.digits[digit])
                resultOperation = self.operation(carry[digit], resultOperation)
                carry[digit*10] =  int(resultOperation/10)
            result[digit] = (carry[digit*10] != 0)

        return result
