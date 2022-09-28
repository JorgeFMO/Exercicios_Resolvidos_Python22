"""
10) Entrar via teclado com o valor de cinco produtos. Após as entradas, 
digitar um valor referente ao pagamento da somatória destes valores. 
Calcular e exibir o troco que deverá ser devolvido.

"""
prod1 = input('1º Produto: ')
prod2 = input('2º Produto: ')
prod3 = input('3º Produto: ')
prod4 = input('4º Produto: ')
prod5 = input('5º Produto: ')

valorRef = input('Qual o Total da Conta: ')

troco = (float(prod1) + float(prod2) + float(prod3) + float(prod4) + float(prod5)) - float(valorRef)

print(troco)
