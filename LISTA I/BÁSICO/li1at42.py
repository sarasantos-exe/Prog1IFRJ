#42 - Listar todos os divisores de um número inteiro.
num = int(input("Digite um número: "))
print([i for i in range(1, num+1) if num %i == 0])
#a lista é gerada utilizando uma list comprehension, que percorre todos os números de 1 até o número digitado pelo usuário (inclusive) e inclui na lista apenas aqueles que são divisores do número (ou seja, aqueles que deixam resto 0 na divisão).