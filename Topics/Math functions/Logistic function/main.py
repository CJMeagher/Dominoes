from math import exp

integer = int(input())
sigmoid = exp(integer) / (exp(integer) + 1)
print(round(sigmoid, 2))
