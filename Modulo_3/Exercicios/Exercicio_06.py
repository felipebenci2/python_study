contador = 0
while True:
    n = int(input('Insira um número: '))
    if n != 0:
       contador += 1
       print('Voce errou, continue tentando')
    else:
        contador
        print(f'Voce acertou em {contador} tentativas')
