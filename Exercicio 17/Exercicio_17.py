"""
17) Faça um algoritmo com três variáveis numéricas (tipo int) que realize a média aritmética da multiplicação desses 3 valores. 
Mostre os resultados na tela. Os mesmos devem ser solicitados ao usuário, digite os valores via teclado.
"""
num1 = int(input('Digite um Numero Inteiro: '))
num2 = int(input('Digite outro Numero Inteiro: '))
num3 = int(input('Digite mais um Numero Inteiro: '))

media = int(((num1 * num2 * num3) / 3))

print(f'Os Numros Digitados foram: {num1}, {num2} e {num3}. A Media da Multiplicação desses 3 Numeros é {media}.')
