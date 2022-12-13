"""
30) O usuário deve digitar seu nome e sua idade. O sistema deverá informar as seguintes mensagens:
Bem vindo NOME você é maior de idade.
Bem vindo NOME você é menor de idade.
Bem vindo NOME você é maior de 65 anos.
"""
nome = input('Qual o seu Nome: ')
idade = int(input('Qual o sua Idade: '))

if idade < 18:
    print(f'Bem vindo {nome} você é menor de idade.')
elif idade >= 18 and idade < 65:
    print(f'Bem vindo {nome} você é maior de idade.')
else:
    print(f'Bem vindo {nome} você é maior de 65 anos')


