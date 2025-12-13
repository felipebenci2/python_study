n1 = float(input('Insira um valor: '))
n2 = float(input('Insira um outro valor: '))
n3 = float(input('Insira o último valor: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Triângulo válido')
else:
    print('Triângulo inválido')
