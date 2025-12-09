nome = input('Digite seu nome: ')
idade = int(input('Digite quantos anos você tem: '))
altura = int(input('Digite sua altura em centímetros. Ex: 169: ')) / 100
peso = float(input('Digite seu peso: '))

resultado = peso / (altura * altura)

print(f'''
--- Dados do Uuário ---
nome = {nome}
idade = {idade}
altura = {altura}
peso = {peso}

Resultado IMC: {resultado: .2f}
 ''')
