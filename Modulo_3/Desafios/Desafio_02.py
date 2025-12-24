contador = 0
soma = 0

while True:
    n = int(input('Insira um número ou digite 0 para encerrar: '))

    if n == 0:
        break

    contador += 1
    soma += n
    print('Número salvo')

if contador > 0:
    media = soma / contador
    print(f'''
Números digitados: {contador}
Média dos números: {media}
''')
else:
    print('Nenhum número digitado')
