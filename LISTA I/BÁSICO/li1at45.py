#45 - Gerar uma senha simples combinando partes do nome e do ano de nascimento.
nome = input("Digite seu nome: ")
ano = input("Digite seu ano de nascimento: ")
senha = nome[:3] + ano[-2:] #pega os três primeiros caracteres do nome e os dois últimos do ano de nascimento.
print(f"Sua senha é: {senha}")