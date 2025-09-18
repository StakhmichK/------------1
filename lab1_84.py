import math

h = float(input("Введіть висоту жердини: "))
a = float(input("Введіть, скільки равлик піднімається за день: "))
b = float(input("Введіть, скільки равлик спускається за ніч: "))

day = int((h - b) / (a - b))

day = math.ceil((h - a) / (a - b)) + 1
print(day)