def producao_camisetas(x):
    a = 12
    b = -30

    print("f(x) = a * x + b")
    print("f(x) = ",a," * ",x," + (",b,")")
    function = a * x + b
    if function < 0:
        print("Resultado negativo para - f(x) = ","\033[31m",function,"\033[0m")
        print("Prejuízo de","\033[31m",function,"\033[0m","se só forem produzidas ",x," camisetas, ou seja, o valor arrecadado com a venda não cobre os custos.")
        return
    if function == 0:
        print("Resultado zerado para - f(x) = ", "\033[33m",function,"\033[0m")
        print("Lucro zerado se forem produzidas ",x," camisetas, ou seja, o valor arrecadado com a venda cobre os custos, mas não gera lucro.")
        return
    else:
        print("Resultado positivo para - f(x) = ", "\033[32m",function,"\033[0m")
        print("Lucro de","\033[32m",function,"\033[0m","se forem produzidas ",x," camisetas, ou seja, o valor arrecadado com a venda cobre os custos e ainda gera lucro.")
        return

x = float(input("Entre com o valor de x: "))
producao_camisetas(x)