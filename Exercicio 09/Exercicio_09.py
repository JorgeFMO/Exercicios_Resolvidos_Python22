"""
9) Entrar via teclado com o valor da cotação do dólar e uma certa quantidade de dólares. 
Calcular e exibir o valor correspondente em Reais (R$).
"""
cotacao = input('Qual a Cotação Atual do Dólar: R$ ')
dolar = input('Digite um valor em Dólar: U$ ')

real = float(dolar) * float(cotacao)

print(real)
