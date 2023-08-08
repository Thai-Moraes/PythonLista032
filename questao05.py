"""
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
"""

valor1 = float(input("Primeiro valor: "))
valor2 = float(input("Segundo valor: "))

print(f"A soma entre número 1 e número 2 é {valor1 + valor2}")
print(f"A subtração do numero 2 pelo numero 1 é {valor2 - valor1}")
print(f"A multiplicação entre número 1 e número 2 é {valor1 * valor2}")
print(f"A divisão entre número 1 e número 2 é {valor1 / valor2}")
print(f"O resto da divisão entre número 1 e número 2 é {valor1 % valor2}")