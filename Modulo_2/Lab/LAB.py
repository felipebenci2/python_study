nome = input('Insira o nome do aluno: ')
nota = float(input('Insira a nota do aluno: '))
if nota > 10 or nota < 0:
    status = 'Nota inválida'
elif nota >= 9:
    status = 'Excelente'
elif nota >= 7:
    status = 'Bom'
elif nota >= 5:
    status = 'Regular'
elif nota < 5:
    status = 'Reprovado'
print(f'''
===== Dados do Aluno =====
Nome = {nome}
Nota = {nota}
Status = {status}
      ''')
