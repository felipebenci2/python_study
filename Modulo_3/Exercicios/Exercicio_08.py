contador = 0
maior = None
while True:
    n = int(input('Insira um valor (0 para sair): '))
    if n == 0:
        break

    if n != 0:
        print('Você errou')
    if maior is None or n > maior:
        maior = n
print(f'Você acertou e o maior número foi {maior}.')
