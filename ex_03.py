# Solicitação dos valores ao usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))

# Cálculo do denominador
denominador_base = a + b + c

# Verificação da validade do denominador
if denominador_base <= 0:
    print("Erro: a soma (a + b + c) deve ser maior que 0 para realizar a raiz quarta.")
else:
    # Cálculo da expressão
    numerador = (a * b) + (c ** d)
    denominador = denominador_base ** (1 / 4)
    G = numerador / denominador

    # Exibição do resultado
    print("O valor de G é:", G)
