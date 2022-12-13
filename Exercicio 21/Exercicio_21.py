"""
21) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 35,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a) comprar apenas latas de 18 litros;
b) comprar apenas galões de 3,6 litros;
c) misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

metro = float(input("Tamanho em metros quadrados (m²) da área a ser pintada: "))
cobertura = float(metro / 6)
lataLitros = 18.0
galaoLitros = 3.6
precoLatas = 80.0
precoGaloes = 35.0
acrescento = 1.1

soLata = cobertura / lataLitros
soGalao = cobertura / galaoLitros

print(f'Você vai prescisar de {cobertura:.2f} litros de tinta.')
if soLata % 1 == 0:
    valorSoLata = soLata * precoLatas
    print(f'Você vai precisar de {soLata:.0f} latas de tintas e o valor vai ficar em R${valorSoLata:.2f}.')
elif soGalao % 1 == 0:
    valorSoGalao = soGalao * precoGaloes
    print(f'Você vai precisar de {soGalao:.0f} galões de tintas e o valor vai ficar em R${valorSoGalao:.2f}.')
else:
    lataresto = cobertura // lataLitros
    valorLataAcres = (lataresto * precoLatas) * acrescento
    resto = math.ceil(cobertura % lataLitros)
    valorGalaoAcres = (resto * precoGaloes) * acrescento
    valorTotalAcres = valorLataAcres + valorGalaoAcres
    print(f'Você vai prescisar de {lataresto:.0f} latas e {resto} galoes de tinta e o valor vai ficar em R${valorTotalAcres:.2f}.')
