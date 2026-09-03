#6 - Informar se um número é par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0: #se o resto da divisão do número por 2 for igual a 0, então o número é par
    print("O número é par.")
else: #se o resto da divisão do número por 2 não for igual a 0, então o número é ímpar 
    print("O número é ímpar.")