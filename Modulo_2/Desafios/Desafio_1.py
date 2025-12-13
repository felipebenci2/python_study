n1 = int(input('Insira um número: '))
if n1 == 0:
    print('O número é zero')
elif n1 > 0 and n1 % 2 == 0:
    print('O número é positivo e par')
elif n1 < 0 and n1 % 2 == 0:
    print('O número é negativo e par')
elif n1 > 0 and n1 % 2 != 0:
    print('O número é positivo e ímpar')
elif n1 < 0 and n1 % 2 != 0:
    print('O número é negativo e ímpar')
