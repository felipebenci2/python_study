nome = input('Insira o nome: ')
idade = int(input('Insira a idade: '))
cidade = input('Insira a cidade que reside: ')
profissao = input('insira a profissão: ')
salario = float(input('Insira o salário: '))
altura = int(input('Insira a altura em cm: ')) / 100
peso = float(input('Insira o peso: '))

print(f''' 
========= CADASTRO =========
Nome: {nome}
Idade: {idade} anos
Profissão: {profissao}
Cidade: {cidade}
Altura: {altura:.2f} m
Peso: {peso:.2f} kg
Salário: R$ {salario:.2f}
============================''')
