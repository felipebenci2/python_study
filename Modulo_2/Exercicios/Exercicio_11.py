idade = int(input('Insira a idade: '))
renda_mes = float(input('Insira a renda bruta mensal: '))
if idade >= 18 and renda_mes >= 2000:
    print('Acesso permitido')
else:
    print('Acesso negado')
