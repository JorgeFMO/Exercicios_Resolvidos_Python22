"""
11) Dona Maria foi comprar uma bolsa. As formas de pagamento que eram oferecidas foram:
a) A vista com 10% de desconto
b) Parcelado em 1+2 vezes sem desconto
c) Dividido em 10 vezes com juros de 5% sobre o valor total
"""
bolsa = input('Valor da Bolsa: ')
vista = float(bolsa) * 0.90
parcelado = float(bolsa) / 3
divi = (float(bolsa) * 1.05) / 10
juros = (float(bolsa) * 1.05)

print(f'O valor da Bolsa é de R${bolsa}, A vista com 10% de desconto fica em R${vista:.2f}.')
print(f'O valor da Bolsa é de R${bolsa}, Parcelamos em 1 de R${parcelado:.2f} e +2 de R${parcelado:.2f}, sem desconto.')
print(f'O valor da Bolsa é de R${bolsa}, Dividimos em 10 vezes de R${divi:.2f} com juros de 5% sobre o valor total de R${juros:.2f}.')



