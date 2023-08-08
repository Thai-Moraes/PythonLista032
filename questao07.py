"""
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações
"""

valor = float(input("Qual o valor da compra?: "))
prestacoes = int(input("Qual o número de prestações?: "))

print("O valor das prestações é de R${:.2f}".format(valor / prestacoes))