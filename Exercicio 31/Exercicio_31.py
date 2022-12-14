"""
31) Elaborar um algoritmo (programa) que calcule o valor fatorial de um número inteiro positivo.
Utilize a estrutura de controle for ...in .
Cálculo do fatorial, exemplo: fatorial de 5 = 5!=1x2x3x4x5= 120
"""
num = int(input('Digite um numero: '))

mult = 1
for fat in list(range(1, num+1)):
    mult = mult * fat
    print(fat)
print(mult)


