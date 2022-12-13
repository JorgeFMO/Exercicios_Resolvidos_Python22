"""
20) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso(p) ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
a = float(input("Qual a sua Altura: "))
sexo = input("Qual o seu Sexo(h/m): ")

if sexo == 'h':
    h = (72.7 * a) - 58
    print(f'Você tem {a} metros de Altura e o seu Peso Ideal é {h:.2f}kg.')
elif sexo == 'm':
    m = (62.1 * a) - 44.7
    print(f'Você tem {a} metros de Altura e o seu Peso Ideal é {m:.2f}kg.')
else:
    print('Erro na Digitação!')
