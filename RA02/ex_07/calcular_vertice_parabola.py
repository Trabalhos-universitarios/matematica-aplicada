import math
from collections import namedtuple

Raizes = namedtuple("Raizes", ["x1", "x2"])
Vertices = namedtuple("Vertices", ["x_v", "y_v"])

def calcular_funcao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
        return
    elif a == 0:
        print("O coeficiente a não pode ser zero.")
        return

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são:", x1, "e", x2)
    print("X1 = ", x1)
    print("X2 = ", x2)
    return Raizes(x1, x2)

def calcular_vertice_parabola(a, b, c):
    x_v = -b / (2*a)
    y_v = a*x_v**2 + b*x_v + c
    print("Os vértices da parábola são:")
    print("Xv =", x_v)
    print("Yv =", y_v)
    return Vertices(x_v, y_v)

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

calcular_funcao_segundo_grau(a, b, c)
result_vertices = calcular_vertice_parabola(a, b, c)

print("O ponto mais alto da parábola é:", result_vertices.y_v)