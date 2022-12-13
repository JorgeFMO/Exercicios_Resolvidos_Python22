"""
14) O restaurante cobra R$23,00 por cada quilo de refeição. 
Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. 
Assuma que a balança já desconte o peso do prato (200 g).
"""
peso = input('Quilos Total da refeição: ')
quiloUni = 23.00
tara = 0.20

pesoReal = (float(peso)-(float(tara)*1000))
programa = ((float(peso)/1000)-float(tara)) * float(quiloUni)

print(f'Total de {pesoReal:.2f}g, Valor a ser pago R${programa:.2f}')