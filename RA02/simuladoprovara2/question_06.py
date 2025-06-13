# 01 - Calculo das raizes da função quadratica
# 02 - Calculo do vertice da função quadratica

import math

def calculation_of_roots(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c

    print("DELTA - ", delta)

    if delta < 0 or a == 0:
        return print("Não existem raízes reais")

    root_to_delta = math.sqrt(delta)
    x1 = (-b -root_to_delta) / (2*a)
    x2 = (-b +root_to_delta) / (2*a)

    if x2 < x1:
        x1Old = x1
        x1 = x2
        x2 = x1Old

    print("X1 = ", x1)
    print("X2 = ", x2)

a = float(input("Enter with A value: "))
b = float(input("Enter with B value: "))
c = float(input("Enter with C value: "))

calculation_of_roots(a, b, c)