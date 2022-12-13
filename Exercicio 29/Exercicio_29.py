"""
29) Elabore um programa que o usuário entre com seu e seu salário. 
Se o salário for menor ou igual a R$1500,00 coloque um acréscimo de 20% de aumento. 
Se for maior que R$1500,00 e menor que R$2500,00 o acréscimo será de 10%, senão o acréscimo será de 5% para os demais valores.
"""
salario = float(input("Qual o seu salário: "))

acres1 = 1.20
acres2 = 1.10
acres3 = 1.05

if salario <= 1500:
    salarioT = salario * acres1
    print(f'O seu Salário é de R${salario:.2f}, mas vamos te dar um Aumento de 20%, o seu Salário vai ficar em R${salarioT:.2f}.')
elif salario > 1500 and salario < 2500:
    salarioT = salario * acres2
    print(f'O seu Salário é de R${salario:.2f}, mas vamos te dar um Aumento de 10%, o seu Salário vai ficar em R${salarioT:.2f}.')
else:
    salarioT = salario * acres3
    print(f'O seu Salário é de R${salario:.2f}, mas vamos te dar um Aumento de 5%, o seu Salário vai ficar em R${salarioT:.2f}.')