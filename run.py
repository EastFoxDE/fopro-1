#!/usr/bin/python3
from a1_class import diffType

x = diffType(2.0, 1.0)
#x2 = x1.sqrt()

print("\nf(x) = 3x^2 - 2x / x+1\n")
y = ((diffType(3.0)*x**2) - (diffType(2.0)*x))/(x + 1.0)
y.show()


#print("X is ", x1.value, " and sqrt(x) = ", x2.value, " and the derivative from x is ", x2.dvalue)
