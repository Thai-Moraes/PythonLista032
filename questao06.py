"""
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês
"""

nome = input("Qual o seu nome?: ")
salario = float(input("Qual o seu salário fixo?: "))
vendas = float(input("Quais foram os totais de vendas efetuadas no mês (em dinheiro)?: "))

print(f"\nNome: {nome}\nSalário (fixo): R${salario}\nSalário (fixo + comissão): R${salario + (vendas * 15/100)}")