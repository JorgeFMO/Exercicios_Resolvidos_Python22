"""
42) Desenvolva um programa que:
a) inicialize uma lista de compras com 5 itens diferentes e exiba
b) Imprima o conteúdo da lista
c) Acrescente mais um item na lista de compras “óleo de canola”
d) Remova da lista de compras o item “Tomate”
e) Qual estrutura de dados vc utilizou? Justifique a sua resposta
           itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate", “Kimojo”]
"""
itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate", "Kimojo"]
a = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate"]

for i, v in enumerate(a):  #42- a)
    print(i, v)

print(itens_compra)  #42- b)

itens_compra.append('óleo de canola')  #42- c)
print(itens_compra)

del(itens_compra[4])  #42- d)
print(itens_compra)

#42- e) Usei 0 "enumerate" para enumarar e 'for' para iterar os itens. Usei o "append" para adicionar mais um item.
# Usei o "del" para excluir um item.



