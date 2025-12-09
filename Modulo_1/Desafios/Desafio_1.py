n1 = int(input('Insira um valor: ')) 
n2 = int(input('Insira um outro valor: '))
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
div_exata = n1 // n2
potencia = n1 ** n2

print(f'''A seguir o produto das funções dos números {n1} e {n2}:
soma = {soma}
subtração = {sub}
multiplicação = {multi}
divisão = {div}
divisão exata = {div_exata}
potência = {potencia}''')
