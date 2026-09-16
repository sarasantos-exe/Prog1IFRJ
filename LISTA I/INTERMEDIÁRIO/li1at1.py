#1 - Ler 10 notas, calcular média, maior e menor valores

#criamos uma lista pra armazenar as nota
notas = []



for i in range(10): #o range(10) vai gerar uma sequência de 0 a 9, ou seja, repetição de 10 números

    nota = float(input(f"Digite a {i + 1}° nota: ")) #pedimos uma nota ao usuário
    #float() converte a entrada do usuário para um número decimal
    #f strings permitem a interpolação de variáveis dentro de strings

    notas.append(nota) #adicionamos a nota dentro da lista de notas

soma = sum(notas) #sum() soma todos os elementos da lista

media = soma / len(notas) #len() retorna a quantidade de elementos da lista
#media é a soma dividida pela quantidade de elementos da lista
#len() é usado para contar quantos elementos existem na lista

maior = max(notas) #max() retorna o maior valor da lista
menor = min(notas) #min() retorna o menor valor da lista



#Mostrando os resultados
print("\n--- RESULTADOS ---") #\n é usado para pular uma linha
# --- RESULTADOS --- é apenas uma string para indicar que os resultados estão sendo mostrados

print(f"Média: {media:.2f}")
print(f"Maior nota: {maior:.2f}")
print(f"Menor nota: {menor:.2f}")