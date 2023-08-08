"""
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
"""

peso = float(input("Qual o seu peso? (em quilos): "))
altura = float(input("Qual a sua altura? (em metros): "))

print(f"O seu peso é de {peso * 1000:.2f} e a sua altura é de {altura * 100:.2f}")