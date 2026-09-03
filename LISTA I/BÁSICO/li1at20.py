#20 - Listar todos os números pares até um limite informado.
limite = int(input("Digite o limite: "))
for i in range(0, limite+1, 2): #o range(0, limite+1, 2) gera uma sequência de números começando em 0 até o limite informado, incrementando de 2 em 2, garantindo que apenas números pares sejam incluídos.
    print(i)