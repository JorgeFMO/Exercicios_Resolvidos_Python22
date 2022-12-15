"""
41) Desenvolva um programa que:
a) Imprima o conteúdo da lista
b) Determine o tamanho conteúdo da lista
c) Coloque em ordem ascendente
d) A lista tem números repetidos? Em caso afirmativo em qual posição?
e) Qual estrutura de dados vc utilizou? Justifique a sua resposta
           numeros = [100, 20, 30, 90, 50, 60, 70, 80, 40, 100, 10]

"""
numeros = [100, 20, 30, 90, 50, 60, 70, 80, 40, 100, 10]

print(numeros)  #41- a)
print(len(numeros))  #41- b)

numeros.sort()
print(numeros)  #41- c)

#41- d)
from collections import defaultdict

# Define a lista de volares:
lista = [100, 20, 30, 90, 50, 60, 70, 80, 40, 100, 10]

# Define o objeto que armazenará os índices de cada elemento:
keys = defaultdict(list);

# Percorre todos os elementos da lista:
for key, value in enumerate(lista):

    # Adiciona o índice do valor na lista de índices:
    keys[value].append(key)

# Exibe o resultado:
for value in keys:
    if len(keys[value]) > 1:
        print(value, keys[value])


#41- e)O módulo collections também tem defaultdict, que se parece com um dicionário, exceto pelo fato de que se você acessar uma chave que não existe,
# um novo valor pode ser gerado automaticamente.




