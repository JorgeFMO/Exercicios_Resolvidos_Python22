"""
22) Desenvolva um programa que receba via teclado um valor e a partir disso faça:
(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;
(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número;
(3) se for os valores 6, 7 e 8, mostre o valor dividido 9.
"""
num = int(input("Digite um Numero(1 a 9): "))

if num == 1 or num == 2 or num == 3:
    calc = num * num
    print(calc)
elif num == 4 or num == 9:
    calc = num ** 0.5
    print(calc)
elif num == 6 or num == 7 or num == 8:
    calc = num /9
    print(calc)
else:
    print(f'O numero 5 não tem calculo!')


