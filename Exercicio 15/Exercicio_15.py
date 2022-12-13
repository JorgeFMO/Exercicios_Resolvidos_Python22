"""
15) Leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a apenas em dias.
"""
ano = input('Digite a quantidade de Anos: ')
meses = input('Digite a quantidade de Anos: ')
dias = input('Digite a quantidade de Anos: ')

prodAno = int(ano) * 365
progMeses = int(meses) * 30
progFim = int(prodAno) + int(progMeses) + int(dias)

print(f'Em um total de {ano} anos, {meses} meses e {dias} dias, o Total Apenas de Dias é de {progFim} dias.')

