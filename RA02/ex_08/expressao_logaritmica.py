import math
def resolver_equacao_exponencial(a, b, k):
    if k <= 0:
        print("Não existe solução real: k deve ser maior que 0.")
        return
    ln_k = math.log(k)
    x = (ln_k - b) / a
    print(f"Solução: x = {x}")
    a = float(input("Informe o coeficiente a: "))
    b = float(input("Informe o coeficiente b: "))
    k = float(input("Informe o valor de k (>0): "))

a = float(input("Informe o coeficiente a: "))
b = float(input("Informe o coeficiente b: "))
k = float(input("Informe o valor de k (>0): "))

resolver_equacao_exponencial(a, b, k)
