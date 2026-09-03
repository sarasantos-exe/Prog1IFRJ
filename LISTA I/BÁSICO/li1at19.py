#19 - Encontrar o maior e o menor entre cinco números informados.
numeros = [] #cria uma lista vazia para armazenar os números
for i in range(5): #repete 5 vezes
    numeros.append(int(input(f"Digite o {i+1}° número: ")))
    # ^ append é um método que adiciona um elemento ao final da lista. Aqui, estamos convertendo a entrada do usuário para inteiro e adicionando à lista.
    # ^ {i+1}° é usado para exibir a posição do número que está sendo solicitado, começando de 1 até 5.
print(f"Maior: {max(numeros)}, Menor: {min(numeros)}")