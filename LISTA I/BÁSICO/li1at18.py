#18 - Somar números lidos até que o usuário digite 0.
soma = 0 #inicializa a variável soma com 0
while True: #inicia um laço infinito, que será interrompido quando o usuário digitar 0
   num = int(input("Digite um número (0 para parar): ")) #lê um número inteiro do usuário
   if num == 0:
      break #interrompe o laço se o usuário digitar 0
   soma += num #adiciona o número digitado à variável soma
print(f"A soma é {soma}") #exibe o resultado da soma