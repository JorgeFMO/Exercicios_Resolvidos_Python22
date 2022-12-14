"""
34) Desenvolva um programa para determinar a média geral do aluno. 
O mesmo deverá receber o nome do aluno, as 2 notas obtidas do aluno nas 2 avaliações. 
Calcular a média de aproveitamento, usando a fórmula da Media e escrever o conceito do aluno de acordo com a tabela de conceitos.
Média é dada pela fórmula: MG = (NP1*4 + NP2*6) / 10
"""
nome = input('Informe o Nome do aluno: ')
np1 = float(input('Informe a nota da NP1 do aluno: '))
np2 = float(input('Informe a nota da NP2 do aluno: '))
media = (np1*4 + np2*6) / 10

if(media < 3):
    print(f'{nome} a sua média é: {media:.1f} . O conceito é D. {nome} você está de DP!')
elif(media >= 3) and (media < 7):
    print(f'{nome} a sua média é: {media:.1f} . O conceito é C. {nome} você está de Exame!')
elif(media >= 7) and (media < 9):
    print(f'{nome} a sua média é: {media:.1f} . O conceito é B. {nome} você está de Aporvado!')
else:
    print(f'{nome} a sua média é: {media:.1f} . O conceito é A. {nome} você está de Aporvado!')
