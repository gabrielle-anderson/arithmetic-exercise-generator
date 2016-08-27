class ProblemSpecification:
    def __init__(self, o1, o2, resultRange, op, adjustments, miscParameters):
        assert (set(o1.digits.keys()) <= set(o2.digits.keys())) or (set(o2.digits.keys()) <= set(o1.digits.keys())), "One operand's set of digits must be a weak superset of the other's."
        self.firstOperandSpecification = o1
        self.secondOperandSpecification = o2
        self.resultExplicitRange = resultRange
        self.operation = op
        self.adjustments = adjustments
        self.miscParameters = miscParameters

    # def result(self):
    #     self.operation(self.operand1.value(), self.operand2.value())

    def __eq__(self, other):
        return self.firstOperandSpecification == other.operand1 and self.secondOperandSpecification == other.operand2 \
               and self.adjustments == other.adjustments and self.miscParameters== other.miscParameters

    def __str__(self):
        result = ""
        result += "Operand 1:\n" + str(self.firstOperandSpecification) + "\n"
        result += "Operand 2:\n" + str(self.secondOperandSpecification) + "\n"
        result += "Operation : " + str(self.operation) + "\n\n"
        result += "Adjustments: " + str(self.adjustments) + "\n\n"
        result += "Miscelaneous parameters: " + str(self.miscParameters) + "\n\n\n"

        return result

    def randomOperands(self):
        firstOperand = self.firstOperandSpecification.randomOperand()
        secondOperand = self.secondOperandSpecification.randomOperand()

        problemAdjustments = self.digitAdjustments(firstOperand, secondOperand)

        validAdjustments = True
        for digit in self.adjustments.keys():
            if (digit in problemAdjustments.keys()):
                validAdjustments = validAdjustments and (self.adjustments[digit] == problemAdjustments[digit])

        if validAdjustments: return (firstOperand, secondOperand)
        else: return self.randomOperands()

    def digitAdjustments(self, firstOperand, secondOperand):
        return {}
