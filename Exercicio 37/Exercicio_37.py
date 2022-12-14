"""
37) Elabore um programa que solicite ao usuário três números diferentes.
Para fazer isso separe seu código em duas funções diferentes: 
Uma função para retornar o maior dos três números e outra função para dobrar os números.
"""

num1 = input('Digite um Numero: ')
num2 = input('Digite outro Numero: ')
num3 = input('Digite mais um Numero: ')

def numMaior(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f'O maior numero é o Numero 1, com o valor de {num1}')
    elif num2 > num1 and num2 > num3:
        print(f'O maior numero é o Numero 2, com o valor de {num2}')
    else:
        print(f'O maior numero é o Numero 3, com o valor de {num3}')

def numDobro(num1, num2, num3):
    print(int(num1) * 2)
    print(int(num2) * 2)
    print(int(num3) * 2)

numMaior(num1, num2, num3)
numDobro(num1, num2, num3)