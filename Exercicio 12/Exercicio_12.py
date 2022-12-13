"""
12) Crie um programa que permita informar o valor total da compra e exiba os valores que Dona Maria irá pagar no total 
em cada uma das formas de pagamento e os valores de cada parcela, caso a mesma opte por dividir.
"""
valorTotal = input('Informe o Valor Total da sua compra: ')
parcela = int(input('Esse Valor Total, em quantas vezes você quer parcelar: '))
programa = float(valorTotal) / int(parcela)
programaVista = float(valorTotal) * 0.95
desc = float(valorTotal) - (float(valorTotal) * 0.95)

if parcela <= 1:
    print(f'Valor à vista tem 5% de desconto, ficando em R${programaVista:.2f}, desconto de R${desc:.2f}.')
else:
    print(f'Valor Total de {valorTotal}, parcelamos em {parcela}X sem juros, cada parcela fica em R${programa:.2f}.')