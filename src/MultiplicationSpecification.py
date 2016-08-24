from ProblemSpecification import ProblemSpecification

class MultiplicationSpecification(ProblemSpecification):
    def digitAdjustments(self, firstOperand, secondOperand):
        result = {}

        digitsFirstOperand = set(firstOperand.digits.keys())
        digitsSecondOperand = set(secondOperand.digits.keys())
        digits = digitsFirstOperand.intersection(digitsSecondOperand)
        digits = [float(digit) for digit in digits]

        for digit in sorted(digits):
            requiresAdjustment = self.operation(firstOperand.digits[digit], secondOperand.digits[digit]) > 9
            result[digit] = requiresAdjustment

        return result
