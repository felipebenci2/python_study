maior = None
listaNum = []
for i in range(3):
    listaNum.append(int(input('Insira um numero: ')))
for n in listaNum:
    if maior is None or n > maior:
        maior = n
print(maior)
