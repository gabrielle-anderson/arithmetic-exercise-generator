from types import *

class Operand:
  digits = {}
  # def __init__(self, *digitsTuple):
  #   assert (digitsTuple.__len__() % 2 == 0)
  #   for x in range(0, (digitsTuple.__len__()/2):
  #       self.digits[digitsTuple[x]] = digitsTuple[x+1]
  #   # assert validDigits()
  def addDigit(self, unit, multiple):
      assert type(unit) is FloatType, "unit is not a float"
      assert type(multiple) is IntType, "multiple is not an integer"
      self.digits[unit] = multiple

  def __eq__(self, other):
    if (self.digits.keys() != other.digits.keys()): return False
    same = True
    for key in self.digits.keys():
        same = same and (self.digits[key] == other.digits[key])
    return same

  def value(self):
      result = 0.0
      for key in self.digits.keys():
          result += (key * self.digits[key])

  # def validDigits(self):
  #
  #     return False