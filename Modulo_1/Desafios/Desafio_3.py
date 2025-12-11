nome = input('Digite seu nome: ')
idade = int(input('Digite quantos anos você tem: '))
altura = int(input('Digite sua altura em centímetros. Ex: 169: ')) / 100
peso = float(input('Digite seu peso: '))

resultado = peso / (altura * altura)

print(f'''
======= RELATÓRIO DE PERFIL =======
Nome: {nome}
Idade: {idade} anos
Altura: {altura:.2f} m
Peso: {peso:.2f} kg
IMC: {resultado:.2f}
===================================
 ''')
