"""
43) Desenvolva um programa em Python que
a) Armazenar o nome, sexo e idade de 10 pessoas.
b) Após a digitação, exibir os dados (nome, sexo e idade) classificados por sexo (crescente),
c) depois classificar por sexo por idade (decrescente) e
d) finalmente classificar por nome (alfabética).
e) Qual estrutura de dados vc utilizou? Justifique a sua resposta
"""
#43-a)
lista = [['SOLANGE', 'F', '34'],
         ['MARCELO', 'M', '36'],
         ['JOAO', 'M', '11'],
         ['MAGNA', 'F', '34'],
         ['JUNIOR', 'M', '6'],
         ['MARIA', 'F', '35'],
         ['LUCAS', 'M', '10'],
         ['GABRIEL', 'M', '7'],
         ['FELIPE', 'M', '10'],
         ['JORGE', 'M', '37']]

listaOrdenada1 = sorted(lista, key = lambda x: (x[1], x[0], x[2]))  #43-b)
for w, y, z in listaOrdenada1:
    print(w, y, z)

print()

listaOrdenada2 = sorted(lista, key = lambda x: (x[1], x[2], x[0]))  #43-c)
for p, q, r in listaOrdenada2:
    print(p, q, r)

print()

for a, b, c in sorted(lista):  #43-d)
    print(a, b, c)

#43-e) : Usei o 'sorted' para ordenar ,
# Usei o 'key = lambda x: (x[], x[], x[]' para definir qual item como prioridade.



