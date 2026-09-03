#27 - Aplicar 10 % de aumento a um salário informado.
salario = float(input("Digite o salário: ")) #o float() converte a entrada do usuário (que é uma string) para um número decimal.
print(f"Novo salário: {salario *1.10:.2f}") #exibe o novo salário, que é calculado multiplicando o salário original por 1.10 (representando um aumento de 10%). O :.2f formata o número para exibir duas casas decimais.