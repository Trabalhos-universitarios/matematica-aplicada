try:
    # Solicita o número de camisetas produzidas
    x = int(input("Digite o número de camisetas produzidas: "))

    # Verifica se o número é válido
    if x < 0:
        print("Erro: a quantidade de camisetas não pode ser negativa.")
    else:
        # Cálculo do lucro
        f = 12 * x - 480

        print(f"\nLucro obtido: R$ {f:.2f}")

        # Interpretação do resultado
        if f > 0:
            print("Resultado: Houve lucro na produção.")
        elif f == 0:
            print("Resultado: A produção atingiu o ponto de equilíbrio.")
        else:
            print("Resultado: Houve prejuízo na produção.")
except ValueError:
    print("Erro: digite um número válido inteiro.")
