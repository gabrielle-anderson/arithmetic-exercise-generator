import os

from AdditionSpecification import *
from DivisionSpecification import *
from SubtractionSpecification import *

from MultiplicationSpecification import *
from SpecificationReaderParameters import SpecificationReaderParameters

plus = SpecificationReaderParameters(os.sep + "Addition", lambda x, y: (x + y), \
                                     lambda o1, o2, resultRange, op, adjustments, miscParameters:
                        AdditionSpecification(o1, o2, resultRange, op, adjustments, miscParameters))
minus = SpecificationReaderParameters(os.sep + "Subtraction", lambda x, y: (x - y), \
                                      lambda o1, o2, resultRange, op, adjustments, miscParameters:
                        SubtractionSpecification(o1, o2, resultRange, op, adjustments, miscParameters))
times = SpecificationReaderParameters(os.sep + "Multiplication", lambda x, y: (x * y), \
                                      lambda o1, o2, resultRange, op, adjustments, miscParameters:
                        MultiplicationSpecification(o1, o2, resultRange, op, adjustments, miscParameters))
divides = SpecificationReaderParameters(os.sep + "Division", lambda x, y: (x % y), \
                                        lambda o1, o2, resultRange, op, adjustments, miscParameters:
                        DivisionSpecification(o1, o2, resultRange, op, adjustments, miscParameters))

additionString = "+"
subtractionString = "-"
multiplicationString = "*"
divisionString = "\\"

