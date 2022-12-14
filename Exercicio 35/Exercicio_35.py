"""
35) Desenvolva um programa que só permita o acesso a pessoas autorizadas (professor, via autenticação) para posteriormente realizar a média do aluno. 
Para isto Considere o programa criado no Exercicio 34.
Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, 
depois faça um (print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo.
"""
loginSecreto = "prof"
senhaSecreta = "123456"
 
while True:
    login = input('Digite seu Login: ')
    if (login == loginSecreto):
        senha = input('Digite sua Senha: ')
        if(senha == senhaSecreta):
            print(f'Bem vindo, Professor!')
        else:
            print(f'Dados Invalidos!')
        break

nome = input('Informe o Nome do aluno: ')
ra = input('Informe o seu RA: ')
turma = input('Informe a sua Turma: ')
np1 = float(input('Informe a nota da NP1 do aluno: '))
np2 = float(input('Informe a nota da NP2 do aluno: '))
media = (np1*4 + np2*6) / 10

if(media < 3):
    print(f'{nome}, RA: {ra} e Turma: {turma}. A sua média é: {media:.1f} . O conceito é D. {nome} você está de DP!')
elif(media >= 3) and (media < 7):
    print(f'{nome}, RA: {ra} e Turma: {turma}. A sua média é: {media:.1f} . O conceito é C. {nome} você está de Exame!')
elif(media >= 7) and (media < 9):
    print(f'{nome}, RA: {ra} e Turma: {turma}. A sua média é: {media:.1f} . O conceito é B. {nome} você está de Aporvado!')
else:
    print(f'{nome}, RA: {ra} e Turma: {turma}. A sua média é: {media:.1f} . O conceito é A. {nome} você está de Aporvado!')
