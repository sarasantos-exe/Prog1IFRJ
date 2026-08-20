nome = "Eduardo"

mensagem = f'Olá, {nome}!'

print (mensagem)



print ("Primeira letra:", nome[0])
# Em Python, os índices começam no 0. 
# Isso significa que nome[0] acessa o primeiro caractere da string "nome".
# Exemplo: se nome = "Sara", então nome[0] = "S".

print ("Última letra:", nome[-1]) ## Quando usamos índices negativos em Python, a contagem é feita de trás para frente.
# O índice -1 representa o último caractere da string, -2 o penúltimo, e assim por diante.
# Exemplo: se nome = "Sara", então nome[-1] = "a".

print ("Tamanho do nome:", len(nome)) # A função len() retorna o número total de caracteres da string.
# Exemplo: se nome = "Sara", len(nome) = 4.