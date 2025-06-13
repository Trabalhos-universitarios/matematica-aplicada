import math

def analisar_funcao_quadratica(a, b, c):
    if a == 0:
        print("Não é uma função do segundo grau.")
        return

    delta = b ** 2 - 4 * a * c
    print(f"Delta (Δ) = {delta}")

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A função possui uma raiz real: x = {x}")
        if a > 0:
            print("A função é positiva exceto em x =", x)
        else:
            print("A função é negativa exceto em x =", x)
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)

        x_menor = min(x1, x2)
        x_maior = max(x1, x2)

        print(f"A função possui duas raízes reais: x1 = {x_menor}, x2 = {x_maior}")

        if a > 0:
            print("A função é positiva para x < {:.2f} e x > {:.2f}".format(x_menor, x_maior))
            print("A função é negativa entre {:.2f} e {:.2f}".format(x_menor, x_maior))
        else:
            print("A função é negativa para x < {:.2f} e x > {:.2f}".format(x_menor, x_maior))
            print("A função é positiva entre {:.2f} e {:.2f}".format(x_menor, x_maior))

# Entrada de dados
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print("\n----- ANÁLISE DA FUNÇÃO -----")
analisar_funcao_quadratica(a, b, c)
