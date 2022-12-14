"""
33) Elaborar um algoritmo (programa) que determine se a pessoa está com no seu Peso Ideal (ou não) e IMC.
Onde o usuário deverá digitar o peso, o sexo e a altura de uma determinada pessoa. 
Após a execução, deverá exibir se esta pessoa está ou não com seu peso ideal. Veja tabela (a) e (b) da relação peso/altura².
Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois faça um (print screen) 
e comentar o(s) resultado(s) do programa após a execução do mesmo.
"""
nome = input('Informe o seu Nome: ')
ra = input('Informe o seu RA: ')
turma = input('Informe a sua Turma: ')
sexo = str(input('Informe o seu Sexo(f/m): '))
peso = float(input('Informe o seu Peso: '))
h = float(input('Informe a sua Altura: '))
imc = peso / (h * h)

if(sexo == "f"):
    if(imc < 19):
        print(f'{nome}, RA: {ra} e Turma: {turma}. Seu IMC é {imc:.0f}. Você esta abaixo do peso.')
    elif (imc >= 19) and (imc < 24):
        print(f'{nome}, RA: {ra} e Turma: {turma}. Seu IMC é {imc:.0f}. Você esta no peso ideal.')
    else:
        print(f'{nome}, RA: {ra} e Turma: {turma}. Seu IMC é {imc:.0f}. Você esta acima do peso.')
if(sexo == "m"):
    if(imc < 20):
        print(f'{nome}, RA: {ra} e Turma: {turma}. Seu IMC é {imc:.0f}. Você esta abaixo do peso.')
    elif (imc >= 20) and (imc < 25):
        print(f'{nome}, RA: {ra} e Turma: {turma}. Seu IMC é {imc:.0f}. Você esta no peso ideal.')
    else:
        print(f'{nome}, RA: {ra} e Turma: {turma}. Seu IMC é {imc:.0f}. Você esta acima do peso.')
