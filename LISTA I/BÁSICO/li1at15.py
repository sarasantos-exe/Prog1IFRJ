#15 - Mostrar apenas o primeiro nome de um nome completo.
nome = input("Digite o seu nome completo: ")
print(f"Seu primeiro nome é {nome.split()[0]}")
#o método split() divide uma string em uma lista de palavras, usando o espaço como separador.
# Ao acessar o índice [0], obtemos a primeira palavra da lista, que corresponde ao primeiro nome.