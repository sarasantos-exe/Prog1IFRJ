#32 - Somar todos os números ímpares de 1 a 50.
soma = sum(i for i in range(1,51) if i % 2 != 0) #a função sum() soma os valores gerados pela expressão dentro dela. A expressão (i for i in range(1, 51) if i % 2 != 0) gera todos os números ímpares de 1 a 50, e a função sum() soma esses números.
print(f"Soma dos ímpares: {soma}")