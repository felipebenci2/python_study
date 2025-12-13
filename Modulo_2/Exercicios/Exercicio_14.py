ano = int(input('Insira o ano: '))
if ano % 400 == 0:
    print('Bissexto')
elif ano % 400 != 0 and ano % 100 == 0:
    print('Não bissexto')
elif ano % 100 != 0 and ano % 4 == 0:
    print('Bissexto')
else:
    print('Não bissexto')
