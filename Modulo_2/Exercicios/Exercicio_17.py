n1 = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))
print(''' 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
      ''')
operacao = input('Insira a opção desejada: ')
if operacao == '1':
    print(f'O resultado da soma de {n1} e {n2} é {n1 + n2}')
elif operacao == '2':
    print(f'O resultado da subtração de {n1} e {n2} é {n1 - n2}')
elif operacao == '3':
    print(f'O resultado da multiplicação de {n1} e {n2} é {n1 * n2}')
elif operacao == '4':
    print(f'O resultado da divisão de {n1} e {n2} é {n1 / n2}')
else:
    print('Selecione uma opção válida.')
