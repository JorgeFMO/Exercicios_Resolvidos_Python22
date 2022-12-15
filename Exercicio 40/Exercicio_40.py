"""
40)
A) Considere o arquivo texto notas_estudantes.dat e desenvolva um programa que calcula a média das notas de cada estudante e imprime o nome e a média de cada estudante. 
B) Considere o arquivo texto notas_estudantes.dat e desenvolva um programa que imprime o nome dos alunos aprovaram sem necessidade de realizar o exame. 
C) Considere o arquivo texto notas_estudantes.dat e desenvolva um programa que determine a nota mínima e máxima da turma. 
   O resultado deve ser mostrado na tela com o nome de cada aluno junto com a sua nota máxima e mínima. 
D) Considere o arquivo texto notas_estudantes.dat e desenvolva um programa que determine e liste os alunos com suas respectivas notas que ficaram de DP.
"""
f = open("alunosAprovados.txt", "w")
f.write("Os alunos aprovados são: ")
f.close()

notas = []

reprovados = []

aluno1 = "José"
p1J = 3.5
tp1J = 0.0

p2J = 5.5
tp2J = 1.5

np1J = p1J + tp1J
np2J = p2J + tp2J
mgJ = (np1J + np2J) / 2

if (mgJ >= 7):
    print(f'{aluno1} você está aprovado, sua média é {mgJ}!')
    f = open("alunosAprovados.txt", "a")
    f.write("\nJosé")
    f.close()
else:
    print(f'{aluno1} você está reprovado, sua média é {mgJ}!')
    reprovados.append(f'{aluno1}, com a nota de {mgJ}')

aluno2 = "Pedro"
p1P = 7.5
tp1P = 2.0

p2P = 7.5
tp2P = 1.0

np1P = p1P + tp1P
np2P = p2P + tp2P
mgP = (np1P + np2P) / 2

if (mgP >= 7):
    print(f'{aluno2} você está aprovado, sua média é {mgP}!')
    f = open("alunosAprovados.txt", "a")
    f.write("\nPedro")
    f.close()
else:
    print(f'{aluno2} você está reprovado, sua média é {mgP}!')
    reprovados.append(f'{aluno2}, com a nota de {mgJ}')

aluno3 = "Suzana"
p1S = 6.5
tp1S = 1.5

p2S = 5.5
tp2S = 1.5

np1S = p1S + tp1S
np2S = p2S + tp2S
mgS = (np1S + np2S) / 2

if (mgS >= 7):
    print(f'{aluno3} você está aprovado, sua média é {mgS}!')
    f = open("alunosAprovados.txt", "a")
    f.write("\nSuzana")
    f.close()
else:
    print(f'{aluno3} você está reprovado, sua média é {mgS}!')
    reprovados.append(f'{aluno3}, com a nota de {mgS}')

aluno4 = "Gisela"
p1G = 8.0
tp1G = 2.0

p2G = 7.5
tp2G = 1.0

np1G = p1G + tp1G
np2G = p2G + tp2G
mgG = (np1G + np2G) / 2

if (mgG >= 7):
    print(f'{aluno4} você está aprovado, sua média é {mgG}!')
    f = open("alunosAprovados.txt", "a")
    f.write("\nGisela")
    f.close()
else:
    print(f'{aluno4} você está reprovado, sua média é {mgG}!')
    reprovados.append(f'{aluno4}, com a nota de {mgG}')

aluno5 = "João"
p1JO = 3.5
tp1JO = 0.0

p2JO = 5.5
tp2JO = 0.0

np1JO = p1JO + tp1JO
np2JO = p2JO + tp2JO
mgJO = (np1JO + np2JO) / 2

if (mgJO >= 7):
    print(f'{aluno5} você está aprovado, sua média é {mgJO}!')
    f = open("alunosAprovados.txt", "a")
    f.write("\nJoão")
    f.close()
else:
    print(f'{aluno5} você está reprovado, sua média é {mgJO}!')
    reprovados.append(f'{aluno5}, com a nota de {mgJO}')

aluno6 = "André"
p1A = 6.0
tp1A = 1.5

p2A = 7.0
tp2A = 1.0

np1A = p1A + tp1A
np2A = p2A + tp2A
mgA = (np1A + np2A) / 2

if (mgA >= 7):
    print(f'{aluno6} você está aprovado, sua média é {mgA}!')
    f = open("alunosAprovados.txt", "a")
    f.write("\nAndré")
    f.close()
else:
    print(f'{aluno6} você está reprovado, sua média é {mgA}!')
    reprovados.append(f'{aluno6}, com a nota de {mgA}')

aluno7 = "Carlos"
p1C = 1.5
tp1C = 0.0

p2C = 4.0
tp2C = 0.0

np1C = p1C + tp1C
np2C = p2C + tp2C
mgC = (np1C + np2C) / 2

if (mgC >= 7):
    print(f'{aluno7} você está aprovado, sua média é {mgC}!')
    f = open("alunosAprovados.txt", "a")
    f.write("\nCarlos")
    f.close()
else:
    print(f'{aluno7} você está reprovado, sua média é {mgC}!')
    reprovados.append(f'{aluno7}, com a nota de {mgC}')

aluno8 = "Natalia"
p1N = 6.0
tp1N = 2.0

p2N = 5.5
tp2N = 1.5

np1N = p1N + tp1N
np2N = p2N + tp2N
mgN = (np1N + np2N) / 2

if (mgN >= 7):
    print(f'{aluno8} você está aprovado, sua média é {mgN}!')
    f = open("alunosAprovados.txt", "a")
    f.write("\nNatalia")
    f.close()
else:
    print(f'{aluno8} você está reprovado, sua média é {mgN}!')
    reprovados.append(f'{aluno8}, com a nota de {mgN}')

aprovados = open("alunosAprovados.txt", "r")
aprovados2 = aprovados.readlines()

for aprovados3 in aprovados2:
    aprovados3 = aprovados3.rstrip()
    print(f"{aprovados3}")

notas.append(f'{mgJ}')
notas.append(f'{mgP}')
notas.append(f'{mgS}')
notas.append(f'{mgG}')
notas.append(f'{mgJO}')
notas.append(f'{mgA}')
notas.append(f'{mgC}')
notas.append(f'{mgN}')

menor = min(notas)
maior = max(notas)
print(f'A menor nota foi {menor}, e a maior nota foi {maior}')

print(f'Os alunos reprovados são: {reprovados}')