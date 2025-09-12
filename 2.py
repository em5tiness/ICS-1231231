import math

a = int(input("Введіть чотирицифрове число: "))
b = str(a)
c = int(b[0] + b[2])
d = int(b[1] + b[3])
e = (c + d) / 2
f = math.sqrt(c * d)

print("Результати для числа", a)
print("Перше двоцифрове число:", c)
print("Друге двоцифрове число:", d)
print("Середнє арифметичне:", round(e, 2))
print("Середнє геометричне:", round(f, 4))