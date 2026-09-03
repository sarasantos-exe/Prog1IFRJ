#34 - Converter um número inteiro para a sua representação binária.
num = int(input("Digite um número: "))
print(bin(num)[2:]) #a função bin() converte um número inteiro para a sua representação binária, e o [2:] remove os dois primeiros caracteres '0b' que indicam que é um número binário.