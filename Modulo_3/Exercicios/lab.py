contador = 0
while True:
    n = int(input('Digite um número qualquer ou 0 pra sair: '))
    if n == 0:
        print('Fim')
        break
    if n != 0:
        contador += 1 
        print('Número salvo')
print(f'Foram digitados {contador} números.')
