import math
import sys

a = float(sys.argv[1])
b = (3 * math.sqrt(3) * a * a) / 2
c = (a * math.sqrt(3)) / 2
e = math.pi * c * c
f = math.pi * a * a

print("Довжина сторони шестикутника:", a)
print("Площа шестикутника:", round(b, 4))
print("Площа вписаного кола:", round(e, 4))
print("Площа описаного кола:", round(f, 4))

