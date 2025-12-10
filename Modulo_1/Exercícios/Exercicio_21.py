from datetime import datetime 
agora = datetime.now()
ano_atual = agora.year

ano_nascimento = int(input('Insira o ano do seu nascimento para verificar sua idade: '))
print(f'Você têm {ano_atual - ano_nascimento} anos.')
