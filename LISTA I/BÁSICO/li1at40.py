#40 - Calcular o valor de cada parcela de uma compra parcelada.
valor = float(input("Valor da compra: "))
parcelas = int(input("Número e parcelas: "))
print(f"Cada parcela: {valor/parcelas:.2f}") #divide o valor da compra pelo número de parcelas para obter o valor de cada parcela, e o :.2f formata o número para exibir duas casas decimais.