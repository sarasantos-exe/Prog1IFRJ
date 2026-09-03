#24 - Verificar se uma palavra é palíndromo.
#palíndromo é uma palavra que pode ser lida da mesma forma de trás para frente, como "arara" ou "radar".
palavra = input("Digite uma palavra: ").lower() #o método lower() converte todos os caracteres de uma string para minúsculas, garantindo que a verificação não seja sensível a maiúsculas e minúsculas.
if palavra == palavra[::-1]:
    print("É palíndromo!")
else:
    print("Não é palíndromo!")