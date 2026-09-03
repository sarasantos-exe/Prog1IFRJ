#37 - Verificar se três segmentos podem formar um triângulo.
a = float(input("Segmento A: "))
b = float(input("Segmento B: "))
c = float(input("Segmento C: "))
if a+b>c and a+c>b and b+c>a:
    print("Forma um triângulo.")
else:
    print("Não forma um triângulo.")