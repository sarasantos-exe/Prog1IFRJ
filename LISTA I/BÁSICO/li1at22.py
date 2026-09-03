#22 - Contar quantos números positivos há em uma lista.
numeros = [10,-3, 5, 0, -1, 8]
positivos = sum(1 for n in numeros if n> 0) #a função sum() soma os valores gerados pela expressão dentro dela. A expressão (1 for n in numeros if n>0) gera 1 para cada número positivo na lista, e a função sum() soma esses 1s, resultando na quantidade de números positivos.
print(f"Quantidade de números positivos {positivos}")