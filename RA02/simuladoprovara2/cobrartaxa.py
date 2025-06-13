def calculaValor(a, x, b):
    return print(f"O valor a ser cobrado é de R$ {a + x * b:.2f}")


taxaFixa = float(input("Digite o valor da taxa: "))
km_percorrido = float(input("Digite a quantidade de km percorridos: "))
valor_por_km = float(input("Digite o valor por km: "))

calculaValor(taxaFixa, km_percorrido, valor_por_km)