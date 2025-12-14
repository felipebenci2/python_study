while True:
    n = int(input('Digite um número até acertar o número oculto: '))
    if n == 0:
        print('Você acertou!')
        break
    else:
        print('Tente novamente!')
        continue
