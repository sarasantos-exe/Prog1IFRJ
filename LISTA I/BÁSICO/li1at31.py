#31 - Criar um menu (1 = sacar, 2 = depositar) e executar a opção escolhida.
opcao = int(input("1 = Sacar, 2 = Depositar: "))
if opcao == 1:
    print("Você escolheu sacar.")
elif opcao == 2: #elif é usado para verificar uma segunda condição, caso a primeira não seja verdadeira.
    print("Você escolheu depositar.")
else:
    print("Opção inválida.")