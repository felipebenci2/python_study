idade = int(input('Insira sua idade: '))
if idade >= 65:
    print('Idoso')
elif idade >= 18:
    print('Adulto')
elif idade >= 13:
    print('Adolescente')
elif idade >= 0:
    print('Criança')
else:
    print('Idade inválida')
