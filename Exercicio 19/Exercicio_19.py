"""
19) Faça um algoritmo com duas variáveis numéricas (tipo int) que realize as 4 operações básicas(soma, subtração, multiplicação e divisão), 
mostre os resultados na tela. Os mesmos devem ser solicitados ao usuário, digite os valores via teclado.
"""
num1 = int(input('Digite um Numero Inteiro: '))
num2 = int(input('Digite outro Numero Inteiro: '))
operador = input('Digite uma Operação Básica: ')

if operador == '+':
    print(num1 + num2)
elif operador == '-':
    print(num1 - num2)
elif operador == '/':
    print(num1 / num2)
elif operador == '*':
    print(num1 * num2)
else:
    print('Operação Invalida!')
