from ProblemSpecification import ProblemSpecification

class MultiplicationSpecification(ProblemSpecification):
    def digitAdjustments(self, firstOperand, secondOperand):
        result = {}

        digitsFirstOperand = set(firstOperand.digits.keys())
        digitsSecondOperand = set(secondOperand.digits.keys())

        for digitFirstOperand in digitsFirstOperand:
            for digitSecondOperand in digitsSecondOperand:
                resultOperation= self.operation(firstOperand.digits[digitFirstOperand], secondOperand.digits[digitSecondOperand])
                resultDigit = digitFirstOperand * digitSecondOperand
                requiresAdjustment = False

                if resultDigit in result.keys():
                    requiresAdjustment = requiresAdjustment or result[resultDigit]
                requiresAdjustment = requiresAdjustment or (resultOperation > 9)
                result[resultDigit] = requiresAdjustment

        return result
