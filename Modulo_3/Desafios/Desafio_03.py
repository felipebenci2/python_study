maior = None

while True:
    n = int(input('Insira um número ou digite 0 para encerrar: '))

    if n == 0:
        break

    print('Número salvo')

    if maior is None or n > maior:
        maior = n

if maior is None:
    print('Nenhum número digitado')
else:
    print(f'Fim! O maior número digitado foi {maior}.')
