from types import *

class Operand:
  def __init__(self):
    self.digits = {}

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
      if (result.is_integer()):
          result = int(result)
      return result

  def __str__(self):
      return str(self.value())

  # def validDigits(self):
  #
  #     return False