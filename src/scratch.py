from AdditionSpecification import *
from DivisionSpecification import *
from SubtractionSpecification import *
from sympy.ntheory import factorint

from Operand import *

print type(factorint(12).keys())

# Addition stuff
operand1 = Operand()
operand1.digits = {1.0:8, 10.0:1}

operand2 = Operand()
operand2.digits = {1.0:3, 10.0:8}

operand3 = Operand()
operand3.digits = {1.0:1}

operand4 = Operand()
operand4.digits = {1.0:3}

problemSpecification = AdditionSpecification(operand1, operand2, [], lambda x, y: (x+y), {}, {})

print problemSpecification.digitAdjustments(operand1, operand2)
print problemSpecification.digitAdjustments(operand1, operand3)
print problemSpecification.digitAdjustments(operand1, operand4)


# Subtraction stuff
operand1 = Operand()
operand1.digits = {1.0:1, 10.0:1, 100.0:1}

operand2 = Operand()
operand2.digits = {1.0:2, 10.0:2}

operand3 = Operand()
operand3.digits = {1.0:1}

operand4 = Operand()
operand4.digits = {1.0:3}

operand5 = Operand()
operand5.digits = {1.0:2}

problemSpecification = SubtractionSpecification(operand1, operand2, [], lambda x, y: (x-y), {}, {})

print str(operand1) + " - " + str(operand2) + ": " + str(problemSpecification.digitAdjustments(operand1, operand2))
print str(operand2) + " - " + str(operand3) + ": " + str(problemSpecification.digitAdjustments(operand2, operand3))
print str(operand2) + " - " + str(operand4) + ": " + str(problemSpecification.digitAdjustments(operand2, operand4))
print str(operand2) + " - " + str(operand5) + ": " + str(problemSpecification.digitAdjustments(operand2, operand5))


# Multiplication stuff

# Division stuff
operand1 = Operand()
operand1.digits = {1.0:5, 10.0:2, 100.0:4}

operand2 = Operand()
operand2.digits = {1.0:5, 10.0:2}

operand3 = Operand()
operand3.digits = {1.0:5}

operand4 = Operand()
operand4.digits = {1.0:3}

operand5 = Operand()
operand5.digits = {1.0:2}

problemSpecification = DivisionSpecification(operand1, operand2, [], lambda x, y: (x/y), {}, {})

print str(operand1) + " / " + str(operand2) + ": " + str(problemSpecification.digitAdjustments(operand1, operand2))
print str(operand1) + " / " + str(operand3) + ": " + str(problemSpecification.digitAdjustments(operand1, operand3))
print str(operand1) + " / " + str(operand4) + ": " + str(problemSpecification.digitAdjustments(operand1, operand4))
print str(operand1) + " / " + str(operand5) + ": " + str(problemSpecification.digitAdjustments(operand1, operand5))