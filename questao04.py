import math

"""
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na 
tela o valor do índice de massa corporal desta pessoa (IMC). 
Fórmula: IMC = peso / altura^2
 - Obs: peso em quilos e altura em metros
"""
peso = float(input("Qual o seu peso? (em quilos): "))
altura = float(input("Qual a sua altura? (em metros): "))

print("O seu IMC é igual a {:.2f}".format(peso / math.pow(altura,2)))


