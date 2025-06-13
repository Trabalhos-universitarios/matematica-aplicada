try:
    # Solicita o tempo em horas
    x = float(input("Digite o tempo de esvaziamento (em horas): "))

    # Verifica se o tempo é válido
    if x < 0:
        print("Erro: o tempo não pode ser negativo.")
    else:
        # Cálculo do nível de água
        f = 100 - 20 * x

        print(f"\nNível da água após {x}h: {f} litros")

        # Interpretação do resultado
        if f > 0:
            print("Ainda há água no tanque.")
        elif f == 0:
            print("O tanque acabou de esvaziar.")
        else:
            print("O tempo excedeu o necessário para esvaziar o tanque (nível de água negativo).")
except ValueError:
    print("Erro: digite um número válido.")
