#14 - Converter graus Celsius em Fahrenheit
c = float(input("Digite a temperatura em °C: "))
f = (c * 9/5) + 32 #porque a fórmula de conversão de Celsius para Fahrenheit é F = (C * 9/5) + 32
print(f"{c}°C equivalem a {f}°F")