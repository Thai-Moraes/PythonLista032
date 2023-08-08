"""
 Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores
"""

numero = int(input("Qual o número total de eleitores?: "))
votos_brancos = int(input("Qual foi o número de votos brancos?: "))
votos_nulos = int(input("Qual foi o número de votos nulos?: "))
votos_validos = int(input("Qual foi o número de votos validos?: "))

print(f"\nVotos totais: {numero}\nVotos brancos: {(100 * votos_brancos)/numero:.2f}%\nVotos nulos: {(100 * votos_nulos)/numero:.2f}%\nVotos validos: {(100 * votos_validos)/numero:.2f}%")



