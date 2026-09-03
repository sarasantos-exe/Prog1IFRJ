#10 - Calcular a idade a partir do ano de nascimento.
ano_nasc = int(input("Digite o seu ano de nascimento: "))
#int converte a entrada do usuário (que é uma string) para um número inteiro.
ano_atual = 2026
idade = ano_atual - ano_nasc
print(f"Você tem {idade} anos. ")