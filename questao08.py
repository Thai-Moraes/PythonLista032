"""
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário
"""

custo = float(input("Custo do produto: "))
percentual = float(input("Acréscimo percentual: "))

print(f"O valor de venda é igual a {custo + (custo * (percentual / 100))}")