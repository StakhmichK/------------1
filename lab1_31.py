# import the math module to use the sqrt() function
import math

# Read two integers from the keyboard
a = int(input("Введіть перший катет a: "))
b = int(input("Введіть другий катет b: "))

# Calculate the hypotenuse using the Pythagorean theorem
c = math.sqrt(a**2 + b**2)

# Output the result
print(f"Гіпотенуза трикутника дорівнює: c")