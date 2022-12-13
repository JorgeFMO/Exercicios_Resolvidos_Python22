"""
16) Leia a idade de uma pessoa expressa em dias e mostre-a em anos, meses e dias.
"""
dias = input('Digite a quantidade de Dias: ')

prodAno = int(dias) // 365
progMeses = int(dias) // 30
progMeses2 = (int(dias) % 365) // 30
progDias = (int(dias) % 365) % 30

print(prodAno, progMeses, progDias)
print(f'Em um Total de {dias} dias é igual: {prodAno} anos, {progMeses} meses e {progDias} dias.')
print(f'Em um Total de {dias} dias, esse Total em anos fica: {prodAno} anos, em meses fica: {progMeses} meses e em dia fica: {dias} dias.')

