a = float(input("Введіть не від'ємне число: "))

integer_part = int(a)
fractional_part = a - integer_part
result = integer_part + int(fractional_part + 0.5)

print("Округлене число: ", result)