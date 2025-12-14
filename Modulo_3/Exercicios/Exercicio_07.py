contador = 0

while True:
    n = int(input('Insira um valor (0 para sair): '))

    if n == 0:
        print(f'Você acertou e usou {contador} números pares')
        break

    if n % 2 == 0:
        contador += 1

    print('Você errou')
