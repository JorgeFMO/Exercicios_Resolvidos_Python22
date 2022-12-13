"""
26) Elabore um programa que mostre os descontos concedidos pela loja ABC em suas mercadorias.
Em compras acima de R$ 300,00 forneça 20% de desconto, entre R$ 200,00 a R$ 299,99 desconto de 10% e abaixo de R$ 199,99 o desconto será de 5%.
Mostre na tela o valor total e o valor final a pagar (com o desconto). Solicite ao usuário que digite os valores via teclado.
"""
compra = float(input("Qual o Valor Total da sua Compra: "))
compra1 = 300.00
compra2 = 200.00
desc1 = 0.80
desc2 = 0.90
desc3 = 0.95

if compra >= compra1:
    compraT = compra * desc1
    print(f'O Valor Total é de R$ {compra:.2f}, mas com o Desconto de 20% fica em R${compraT:.2f}.')
elif compra < compra1 and compra > compra2:
    compraT = compra * desc2
    print(f'O Valor Total é de R$ {compra:.2f}, mas com o Desconto de 10% fica em R${compraT:.2f}.')
else:
    compraT = compra * desc3
    print(f'O Valor Total é de R$ {compra:.2f}, mas com o Desconto de 5% fica em R${compraT:.2f}.')
