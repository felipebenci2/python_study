letra = input('Insira uma letra: ')
if letra in 'aeiouAEIOU':
    print('Vogal')
elif letra in '123456789':
    print('Insira somente LETRAS')
else:
    print('Consoante')
