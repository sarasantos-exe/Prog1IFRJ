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




# Inteiros representam números sem parte decimal.
idade = 35
anos_para_aposentadoria = 65 - idade
print("Faltam", anos_para_aposentadoria, "anos para a aposentadoria.")

dobro = idade * 2
print("O dobro da idade é:", dobro)




# Floats são números com parte decimal.
altura = 1.75
peso = 70.0

imc = peso / (altura ** 2 )
print("Seu IMC é:", imc)




# Booleanos representam verdadeiro ou falso.
tem_carteira = True
tem_veiculo = False

# Podemos fazer verificações lógicas.
pode_dirigir = tem_carteira and tem_veiculo
print("Pode dirigir:", pode_dirigir)




# Números complexos possuem parte real e imaginária.
z = 2 + 3j

print ("Número complexo:", z)
print("Parte real:", z.real)
print("Parte imaginária:", z.imag)

# Podemos somar complexos.
w = 1 - 1j
soma = z + w
print("Soma dos complexos:", soma)