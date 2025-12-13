for c in range (3):
    senha = input('Senha: ')
    if senha == 'admin123':
        print('Acesso liberado')  
        break  
    else:
        print('Senha incorreta')
else:
    print('Usuário bloqueado')
