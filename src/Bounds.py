from random import randint
from types import *

class Bounds:
    def __init__(self, lowerBound, upperBound):
        assert type(lowerBound) is IntType, "lowerBound " + str(lowerBound) + " is not an integer"
        assert type(upperBound) is IntType, "upperBound is not an integer"

        assert lowerBound >= 0, "lowerBound must be non-negative"
        assert upperBound >= 0, "upperBound must be non-negative"
        assert lowerBound <= upperBound, "lowerBound must be less than upperBound"

        self.lowerBound = lowerBound
        self.upperBound = upperBound

    def __str__(self):
        return "LB: " + str(self.lowerBound) + " UB: " + str(self.upperBound)

    def randomInt(self):
        return randint(self.lowerBound, self.upperBound)