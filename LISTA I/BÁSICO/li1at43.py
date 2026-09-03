#43 - Contar a quantidade de letras em um nome, ignorando espaços.
nome = input("Digite seu nome: ")
print(f"Quantidade de letras: {len(nome.replace(' ', ''))}")
#o método replace() substitui todos os espaços em branco por uma string vazia, e a função len() conta quantos caracteres restaram na string resultante.