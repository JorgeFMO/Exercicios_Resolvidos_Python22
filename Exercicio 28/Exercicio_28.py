"""
28) Nesse programa o usuário deve entrar com um número e o sistema retornar se ele é divisível por 10 ou 
se é divisível por 5 ou se é divisível por 2, caso contrário retornar que o valor não é divisível por nenhum desses valores.
"""
valor = int(input("Digite um Valor: "))

if ((valor % 10 == 0) and (valor % 5 == 0) and (valor % 2 == 0)):
    print(f'{valor} é divisivel por 10, 5 e 2.')
elif (valor % 10 == 0):
    print(f'{valor} é divisivel por 10.')
elif (valor % 5 == 0):
    print(f'{valor} é divisivel por 5.')
elif (valor % 2 == 0):
    print(f'{valor} é divisivel por 2.')
else:
    print(f'{valor} não é divisivel por 10, nem 5 e nem por 2.')
