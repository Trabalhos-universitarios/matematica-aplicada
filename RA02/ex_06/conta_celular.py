def conta_celular(x):
    a = 0.4
    b = -30

    print("f(x) = a * x + b")
    print("f(x) = ",a," * ",x," + (",b,")")
    function = a * x + b
    if function < 0:
        print("Resultado negativo para - f(x) = ", function)
        print("Cobrança extra negativa significa que não houve cobrança extra, ou seja, o usuário ainda está dentro da franquia ou tem um crédito de R$", function)
    if function == 0:
        print("Resultado zerado para - f(x) = ", function)
        print("Cobrança extra zerada significa que o usuário atingiu exatamente o limite da franquia, ou seja, não tem crédito nem débito.")
    else:
        print("Resultado positivo para - f(x) = ", function)
        print("Cobrança extra positiva significa que o usuário excedeu o limite da franquia e terá que pagar R$", function)




x = float(input("Entre com o valor de x: "))

conta_celular(x)