def calcular_vertice(a, b, c):
    if a == 0:
        print("Não é uma função do segundo grau.")
        return

    x_v = -b / (2 * a)
    y_v = a * (x_v ** 2) + b * x_v + c
    print(f"Vértice da parábola: ({x_v}, {y_v})")

# Entrada de dados
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print("\n----- VÉRTICE -----")
calcular_vertice(a, b, c)
