import math
from collections import namedtuple

Raizes = namedtuple("Raizes", ["x1", "x2"])
Vertices = namedtuple("Vertice", ["x_v"])


def calcular_funcao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
        return
    elif delta == 0:
        print("A equação possui apenas uma raiz real.")
        print("X = ", calcula_bhaskara_raiz_unica(a, b).x_v)
        return
    elif a == 0:
        print("O coeficiente a não pode ser zero.")
        return
    elif a > 0:
        print("A concavidade da parábola é para cima.")
    elif a < 0:
        print("A concavidade da parábola é para baixo.")

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da equação são:", x1, "e", x2)
    print("X1 = ", x1)
    print("X2 = ", x2)
    return Raizes(x1, x2)

def calcula_bhaskara_raiz_unica(a, b):
    x_v = -b / (2*a)
    return Vertices(x_v)

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

calcular_funcao_segundo_grau(a, b, c)