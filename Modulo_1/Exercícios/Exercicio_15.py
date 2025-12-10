salario = float(input('Insira o saário: '))
porcento = int(input('Insira a porcentagem do aumento: '))
aumento = (salario * porcento) / 100
novoSalario = salario + aumento
print(f'O novo salário com {porcento}% de aumento seria de R${novoSalario}, resultando em um aumento de R${aumento}.')
