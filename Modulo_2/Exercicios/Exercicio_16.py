n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira o último número: '))

if n1 > n2 and n1 > n3:
    print(f'O número {n1} é maior que {n2} e {n3}.')
elif n2 > n3 and n2 > n1:
    print(f'O número {n2} é maior que {n1} e {n3}.')
elif n3 > n1 and n3 > n2:
    print(f'O número {n3} é maior que {n1} e {n2}.')
elif n1 == n2 and n1 == n3 and n2 == n3:
    print('Existem números iguais')
