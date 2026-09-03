#39 - Mostrar o dia da semana correspondente a um número de 1 a 7.
dias = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
num = int(input("Digite um número (1-7): "))
print(dias[num-1]) #subtraímos 1 do número digitado pelo usuário para acessar o índice correto da lista, já que a lista começa no índice 0.