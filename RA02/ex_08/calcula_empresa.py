import math


def calcular_t(Q0, r, c, M):
    # Verificar restrições
    if Q0 <= 0:
        return "Erro: Q0 deve ser maior que 0."
    if M <= 0:
        return "Erro: M deve ser maior que 0."
    if r == 0:
        return "Erro: r não pode ser zero."

    try:
        t = (math.log(M / Q0) - c) / r
        return f"O valor de t é aproximadamente {t:.2f} meses."
    except ValueError:
        return "Erro: valor inválido no logaritmo. Verifique se M/Q0 é positivo."


# Exemplo de uso:
Q0 = float(input("Digite Q0 (quantidade inicial de dados): "))
r = float(input("Digite r (taxa de crescimento): "))
c = float(input("Digite c (constante de ajuste): "))
M = float(input("Digite M (quantidade final de dados desejada): "))

resultado = calcular_t(Q0, r, c, M)
print(resultado)
