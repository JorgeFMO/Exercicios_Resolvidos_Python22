"""
23) Faça um algoritmo que calcule a média do aluno. 
Ele deve entrar com seu nome, ra, nota 1 enota 2. O sistema deverá informar a ele as seguintes mensagens:
a) Se a média for maior ou igual a sete: Parabéns, você está aprovado!
b) Se a média for menor que sete: Você ainda tem uma chance! Estude mais para o exame.
"""
nome = input("Qual o seu Nome Completo: ")
ra = input("Qual o seu RA: ")
nota1 = float(input("Insira a Nota 1: "))
nota2 = float(input("Insira a Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'{nome}, sua Media foi {media}.')
    print(f'Parabéns, você foi aprovado!')
else: 
    print(f'{nome}, sua Media foi {media}.')
    print(f'Você ainda tem uma chance! Estude mais para o exame.')   


