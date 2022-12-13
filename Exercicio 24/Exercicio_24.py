"""
24) Altere o algoritmo anterior (Exercicio_23) para que o usuário entre com a nota do exame. 
Lembre-seque deve se realizar a média aritmética entre a média e a nota do exame. 
O sistema deveráinformar a ele as seguintes mensagens:
a) Se a média for maior ou igual a cinco: Parabéns, você aproveitou a sua chance! Está aprovado.
b) Se a média for menor que cinco: Estude mais para a próxima. Você não alcançou o mínimo necessário.
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
    exame = float(input("Insira a Nota do Exame: "))
    notaFinal = (media + exame) / 2
    if notaFinal >= 5:   
        print(f'{nome}, sua Media foi {media}.')
        print(f'Parabéns, você aproveitou a sua chance! Está aprovado!')
    else:
        print(f'{nome}, sua Media foi {media}.')
        print(f'Estude mais para a próxima. Você não alcançou o mínimo necessário.')

