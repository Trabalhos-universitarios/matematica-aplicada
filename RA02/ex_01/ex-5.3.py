# Solicita ao usuário o total de minutos usados
try:
    x = float(input("Digite o total de minutos usados no mês: "))

    # Verificação da validade da entrada
    if x < 0:
        print("Erro: o número de minutos não pode ser negativo.")
    else:
        # Cálculo da função f(x)
        f = 0.4 * x - 30

        # Exibição do valor calculado
        print(f"\nCobrança extra (f(x)) = R$ {f:.2f}")

        # Interpretação do resultado
        if f > 0:
            print("Você ultrapassou a franquia. Será cobrada uma taxa extra.")
        elif f == 0:
            print("Você usou exatamente a franquia. Não há cobrança extra.")
        else:
            print("Você usou menos que a franquia. Nenhuma taxa extra será cobrada.")

except ValueError:
    print("Erro: digite um número válido.")
