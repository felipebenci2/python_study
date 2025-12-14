idade = int(input('Insira uma idade: '))
if idade < 0 or idade > 120:
    print('Idade inválida')
elif idade >= 65:
    print('Idoso')
elif idade >= 18:
    print('Adulto')
else:
    print('Criança')
