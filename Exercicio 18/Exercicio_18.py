"""
18) Faça um algoritmo que mostre os descontos concedidos pela loja ABC em suas mercadorias.
Em compras acima de 300,00 forneça 20% de desconto, para 200,00 desconto de 15% e acima de 100,00 o desconto será de 10%. 
Atribua valores as variáveis compra1, compra2 e compra3.
Mostre na tela o valor total e o valor com o devido desconto. Os mesmos devem ser solicitados ao usuário, digite os valores via teclado.

"""
compra = float(input("Qual o Valor Total da sua Compra: "))
compra1 = 300.00
compra2 = 200.00
compra3 = 100.00
desc1 = 0.80
desc2 = 0.85
desc3 = 0.90

if compra >= compra1:
    compraT = compra * desc1
    print(f'O Valor Total é de R$ {compra:.2f}, mas com o Desconto de 20% fica em R${compraT:.2f}.')
elif compra < compra1 and compra > compra3:
    compraT = compra * desc2
    print(f'O Valor Total é de R$ {compra:.2f}, mas com o Desconto de 15% fica em R${compraT:.2f}.')
else:
    compraT = compra * desc3
    print(f'O Valor Total é de R$ {compra:.2f}, mas com o Desconto de 10% fica em R${compraT:.2f}.')
    