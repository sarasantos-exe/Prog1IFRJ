#16 - Exibir a tabuada de 1 a 10 para um número fornecido.
num = int(input("Digite um número: "))
for i in range(1,11): #for é uma estrutura de repetição que permite executar um bloco de código várias vezes.
#A função range(1,11) gera uma sequência de números de 1 a 10 (o último número é exclusivo).
#i representa cada número da sequência gerada pelo range, e o bloco de código dentro do for será executado para cada valor de i.
#in é usado para verificar se um elemento está presente em uma sequência (como uma lista, tupla ou string). No caso do for, in é usado para iterar sobre os elementos da sequência gerada pelo range.
    print(f"{num} x {i} = {num*i}")