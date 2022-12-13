"""
13) Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento. Exiba quantos
litros o mesmo conseguiu colocar no tanque.
"""
valor = input('Qual o valor gasto com Gasolina: ')
litroUni = input('Valor do Litro da Gasolina: ')
programa = float(valor) / float(litroUni)

print(f'Foram gastos R${valor} , para {programa:.2f} litros de Gasolina.')