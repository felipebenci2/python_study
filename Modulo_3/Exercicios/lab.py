soma = 0
while True:
    n = int(input('Digite números aleatórios ou 0 p/ sair: '))
    if n == 0:
        print('Fim')
        break
    if n != 0:
        soma += n
        print('Número salvo')
print(f'A soma dos números foi de {soma}')
