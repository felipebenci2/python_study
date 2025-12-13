idade = int(input('Insira a idade: '))
renda = float(input('Insira a renda: '))
score = float(input('Insira seu score de crédito: '))
if idade >= 18 and renda >= 2500 and score >=700:
    print('Crédito aprovado')
else:
    print('Crédito negado')
