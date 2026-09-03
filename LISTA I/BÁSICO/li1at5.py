#5 - Calcular o IMC a partir de peso e altura
#O cálculo do IMC (Índice de Massa Corporal) é feito dividindo o peso (em kg) pela altura
#(em metros) ao quadrado.Ou seja: IMC = peso / (altura ** 2)
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura **2)
print(f"Seu IMC é {imc:.2f}") # > O :.2f formata o número para mostrar apenas
#duas casas decimais.