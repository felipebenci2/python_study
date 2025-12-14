from datetime import date, datetime 
while True:
        print('''
    ===== Menu =====
    1- Olá
    2- Data atual
    3- Sair
    ''')
        opcao = input('Insira uma opçao: ')
        if opcao == '1' or 'o' in opcao.lower():
                print('''
    ===== Menu =====
    1- Olá
    2- Data atual
    3- Sair
    ''')
                print('Olá')
        elif opcao == '2' or 'data' 'atual' in opcao.lower():
                print('''
    ===== Menu =====
    1- Olá
    2- Data atual
    3- Sair
    ''')
                hoje = date.today()
                print(hoje)
        elif opcao == '3' or 'sair' in opcao.lower():
                print('Fim')
                break
        else:
                print('Insira uma opçao válida')
