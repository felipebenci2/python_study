n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
resultado = n1 - n2
if resultado > 20:
    print('Diferença maior que 20')
elif resultado < 20:
    print('Diferença menor que 20')
else:
    print('Diferença igual a 20')
