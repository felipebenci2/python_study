senha_correta = "python"
for i in range(1,4):
    senhaDigitada = input('Insira uma senha: ')
    if senhaDigitada == senha_correta and i == 1:
        print(f'Acesso liberado. Foi necessaria {i} tentativa.')
        break
    elif senhaDigitada == senha_correta and i > 1:
        print(f'Acesso liberado. Foram necessarias {i} tentativas.')
        break
    elif senhaDigitada != senha_correta and i == 1:
        print(f'{i} tentativa incorreta. Tente novamente')
    elif senhaDigitada != senha_correta and i > 1 and i < 4:
        print(f'{i} tentativas incorretas. Tente novamente')
else:
    print(f'Acesso bloqueado. {i} tentativas incorretas.')
