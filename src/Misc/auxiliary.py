from sympy.ntheory import factorint

def hasRecurringDecimal(number):
    factors = set(factorint(number).keys())
    acceptablePrimeFactors = set([2,3,5])

    return factors.issubset(acceptablePrimeFactors) and 3 in factors

def cellValues(rowCells):
    return [cell.value for cell in rowCells]

def formatProblem(problemString, x, y):
    return str(x) + " " + problemString + " " + str(y)