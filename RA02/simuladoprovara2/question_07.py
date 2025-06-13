import math

def calculation_of_log(a, b, x):
    if x < 0 and a == 0 and b < 0 and b == 1:
        return print("Error")

    return a * math.log(x, b)

a = float(input("Enter with A value: "))
b = float(input("Enter with B value: "))
x = float(input("Enter with X value: "))

print(calculation_of_log(a, b, x))