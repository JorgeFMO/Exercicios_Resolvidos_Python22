"""
38) Elaborar um programa que determine o cálculo do salário e retorna o valor a ser pago conforme o número de horas trabalhadas. 
Lembrando que as mesmas serão digitadas.
Seguem as regras de negocio
Caso a quantidade de horas trabalhadas é menor ou igual a 40, o valor do salario é apenas multiplicando a quantidade de horas pelo valor de cada hora trabalhada.
Caso o trabalhar tenha horas extras, é adicionado ao salário um valor pelas horas extras.
Dica utilizar a função calcular_pagamento (HT, VH)
"""

ht = int(input('Digite a quantidade de horas trabalhadas: '))
vh = float(input('Digite o valor da hora: '))

def calcularPagamento(ht, vh):
    total = 0
    while total < 35:
        if (ht <= 40):
            print(f'Seu salario será R${ht * vh}')
            break
        else:
            he = float(input('Digite o valor da hora extra: '))
            print(f'Seu salario será R${(ht * vh) + he}')
            break
    
calcularPagamento(ht, vh)


