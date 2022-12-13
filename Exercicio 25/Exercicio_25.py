"""
25) Desenvolva um programa que receba via teclado um valor e a partir disso faça:
(1) se o valor for 1 e 2, mostre o valor elevado ao cubo;
(2) se o valor for múltiplo de 3 mostre o fatorial desse número;
(3) se o valor for os valores 4, 5, 7 ou 8, mostre o valor dividido 9. Caso não seja nenhum dos valores, informe como “valor inválido”.
"""
num = int(input("Digite um Numero: "))

if (num % 3) == 0:
    for mult3 in range(1, num+1):
        if (mult3 % 3 == 0):
            print(f'{mult3} é multipo de 3')
elif num == 1 or num == 2:
    calc = num ** 3
    print(calc)
elif num == 4 or num == 5 or num == 7 or num == 8:
    calc = num / 9
    print(calc)
else:
    print("Valor inválido.")
