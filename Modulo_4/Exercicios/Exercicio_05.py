listaNum = []
soma = 0
media = 0
while True:
    n = int(input('Insira numeros aleatorios ou digite 0 para sair: '))
    if n == 0:
        break
    else:
        listaNum.append(n)
        soma += n
        media = soma / len(listaNum)
print(f'Lista dos numeros digitados: {listaNum}')
print(f'Soma dos numeros: {soma}')
print(f'A media dos numeros digitados: {media}')
