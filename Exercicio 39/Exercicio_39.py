"""
38) Desenvolver um programa que determine a área de uma figura geométrica: retângulo, triangulo ou círculo.
Para isto utilize 3 funções que calculam a área de um objeto enviando parâmetros para as funções conforme a entrada do usuário
e retornando o valor calculado da área de acordo com a escolha do usuário.
No programa deve ter um menu de opções que fica dentro de um laço while, esta é uma forma bem eficiente de para se criar um menu.
"""
import math

fg = str(input('Digite qual figura geométrica, você deseja calcular a áera(retangulo, triangulo ou circulo): '))

def x(fg):
    while fg:
        if fg == 'retangulo':
            h = float(input('Digite a altura do retangulo: '))
            b = float(input('Digite a base do retangulo: '))
            calcRet = h * b
            print(f'A área do seu retangulo é: {calcRet:.1f}')
            break
        elif fg == 'triangulo':
            h = float(input('Digite a altura do triangulo: '))
            b = float(input('Digite a base do triangulo: '))
            calcTri = (h * b) / 2
            print(f'A área do seu retangulo é: {calcTri:.1f}')
            break
        elif fg == 'circulo':
            r = float(input('Digite o raio do circulo: '))            
            calcCir = math.pi * (r * r)
            print(f'A área do seu retangulo é: {calcCir:.1f}')
            break
        else:
            print(f'Digite uma figura geométrica válida(retangulo, triangulo ou circulo)!')
            break

x(fg)