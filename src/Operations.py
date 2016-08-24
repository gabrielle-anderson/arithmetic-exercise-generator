# plus = lambda x, y: Fraction(x.numerator*y.denominator + y.numerator*x.denominator, x.denominator*y.denominator)
# minus = lambda x, y: Fraction(x.numerator*y.denominator - y.numerator*x.denominator, x.denominator*y.denominator)
# times = lambda x, y: Fraction(x.numerator*y.numerator, x.denominator*y.denominator)
# divides = lambda x, y: Fraction(x.numerator*y.denominator, x.denominator*y.numerator)

plus = lambda x, y: (x+y)
minus = lambda x, y: (x-y)
times = lambda x, y: (x*y)
divides = lambda x, y: (x/y)

operations = {"plus": plus, "minus": minus, "times": times, "divides": divides}
