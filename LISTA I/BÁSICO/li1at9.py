#9 - Contar quantas letras “a” existem em uma frase
frase = input("Digite uma frase: ")
#o método count() conta quantas vezes um determinado caractere aparece em uma string.
print(f"A letra 'a' aparece {frase.lower().count('a')} vezes. ")