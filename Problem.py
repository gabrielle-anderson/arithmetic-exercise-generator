class Problem:
    operand1 = {}
    operand2 = {}
    def __init__(self, o1, o2, op):
        self.operand1 = o1
        self.operand2 = o2
        self.operation = op
    def result(self):
        self.operation(self.operand1.value(), self.operand2.value())
    def __eq__(self, other):
        return self.operand1 == other.operand1 and self.operand2 == other.operand2
