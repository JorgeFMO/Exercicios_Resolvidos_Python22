"""
27) Desenvolva um programa que receba via teclado um valor e a partir disso faça:
(1) se for um valor negativo, mostre o módulo (valor sem sinal) do valor;
(2) se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles;
(3) Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5
"""
valor = float(input("Digite um Valor: "))

if valor < 0:
    valorposi = valor - (valor) - (valor)
    print(valorposi)
elif valor > 10:
    outroValor = float(input("Digite outro Valor: "))
    calc = valor - outroValor
    print(f' Adiferença entre {valor} e {outroValor} é {calc:.2f}.')
else:
    calc = valor / 5
    print(f'O Valor {valor} dividido por 5 é {calc}.')

