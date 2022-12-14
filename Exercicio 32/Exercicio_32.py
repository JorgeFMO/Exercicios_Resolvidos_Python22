"""
32) Elaborar um algoritmo (programa) que leia as notas de 5 alunos e retorne a maior nota da turma.
"""
aluno1 = input('Qual o seu Nome: ')
aluno1Nota = float(input('Qual a sua Nota: '))
aluno2 = input('Qual o seu Nome: ')
aluno2Nota = float(input('Qual a sua Nota: '))
aluno3 = input('Qual o seu Nome: ')
aluno3Nota = float(input('Qual a sua Nota: '))
aluno4 = input('Qual o seu Nome: ')
aluno4Nota = float(input('Qual a sua Nota: '))
aluno5 = input('Qual o seu Nome: ')
aluno5Nota = float(input('Qual a sua Nota: '))

print()

if aluno1Nota > aluno2Nota and aluno1Nota > aluno3Nota and aluno1Nota > aluno4Nota and aluno1Nota > aluno5Nota:
    print(f'{aluno1} a sua Nota foi a Maior, sua Nota foi {aluno1Nota}')
elif aluno2Nota > aluno1Nota and aluno2Nota > aluno3Nota and aluno2Nota > aluno4Nota and aluno2Nota > aluno5Nota:
    print(f'{aluno2} a sua Nota foi a Maior, sua Nota foi {aluno2Nota}')
elif aluno3Nota > aluno1Nota and aluno3Nota > aluno2Nota and aluno3Nota > aluno4Nota and aluno3Nota > aluno5Nota:
    print(f'{aluno3} a sua Nota foi a Maior, sua Nota foi {aluno3Nota}')
elif aluno4Nota > aluno1Nota and aluno4Nota > aluno2Nota and aluno4Nota > aluno3Nota and aluno4Nota > aluno5Nota:
    print(f'{aluno4} a sua Nota foi a Maior, sua Nota foi {aluno4Nota}')
else:
    print(f'{aluno5} a sua Nota foi a Maior, sua Nota foi {aluno5Nota}')