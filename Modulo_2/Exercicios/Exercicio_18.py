for c in range (3):
    senha = input('Insira a senha: ')
    if senha == 'python123':
        print('Acesso liberado')
        break
    else:
        print('Senha incorreta')
else:
    print('Acesso bloqueado, entre em contato com a supervisão')
