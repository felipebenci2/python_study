valor_real = float(input('Insira o valor em REAIS(R$) para fazer a conversão: '))
valor_euro = valor_real / 6.42
valor_libra = valor_real / 7.34
valor_iene = valor_real / 0.035

print(f''' 
O valor de R${valor_real:.2f} convertido para:
Euro: €{valor_euro:.2f}
Libra Esterlina: £{valor_libra:.2f}
Iene: ¥{valor_iene:.2f}
''')
