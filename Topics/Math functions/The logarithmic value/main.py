import math

integer = int(input())
base = int(input())

if base == 1 or base <= 0:
    print(round(math.log(integer), 2))
else:
    print(round(math.log(integer, base), 2))
