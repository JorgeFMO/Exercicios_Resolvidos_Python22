"""
36) Elabore um programa que solicite o nome do usuário e a idade do usuário, depois disso exiba a mensagem:“{nome} possui {idade} anos.”. 
Esta mensagem deve ser escrita em uma função.
"""

nome = input('Informe o seu Nome: ')
idade = int(input('Informe a sua Idade: '))

def x(nome, idade):
    print(f'{nome} possui {idade} anos.')

x(nome, idade)
