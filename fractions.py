class Fraction:
  numerator = 1
  denominator = 1
  def __init__(self, n, d):
    self.numerator = n
    self.denominator = d
  def __eq__(self, other):
      return self.numerator == other.numerator and self.denominator == other.denominator
