from datetime import date, datetime 
while True:
        print('''
    ===== Menu =====
    1- Olá
    2- Data atual
    3- Sair
    ''')
        opcao = input('Insira uma opçao: ')

        if opcao == '1' or opcao == 'ola':
                print('Olá')

        elif opcao == '2' or opcao == 'Data' or opcao == 'Atual':
                hoje = date.today()
                print(hoje)

        elif opcao == '3' or opcao == 'Data':
                print('Fim')
                break
        else:
                print('Insira uma opçao válida')
