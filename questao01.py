'''
 Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom
'''

valor = float(input("Qual o valor da conta?: "))
print(f"A conta junto com as gorjetas do garçom (10%) é igual a {valor + (valor * 10/100)}")