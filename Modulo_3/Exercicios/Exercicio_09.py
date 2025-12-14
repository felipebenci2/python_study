from datetime import date, datetime 
while True:
        print('''
    ===== Menu =====
    1- Olá
    2- Data atual
    3- Sair
    ''')
        opcao = input('Insira uma opçao: ')

        if opcao == '1' or 'olá' in opcao.lower():
                print('Olá')

        elif opcao == '2' or 'data' in opcao.lower():
                hoje = date.today()
                print(hoje)
                
        elif opcao == '3' or 'sair' in opcao.lower():
                print('Fim')
                break
        else:
                print('Insira uma opçao válida')
