#30 - Identificar se um caractere lido é vogal ou consoante.
letra = input("Digite uma letra: ").lower() #o método lower() converte todos os caracteres de uma string para minúsculas, garantindo que a verificação não seja sensível a maiúsculas e minúsculas.
if letra in "aeiou":
    print("É vogal!")
else:
    print("É consoante!")