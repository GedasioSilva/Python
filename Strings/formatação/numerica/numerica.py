#fazendo formatação Númerica adicionar virgulas e pontos

salario = 1789

#colocando casas decimais 
print(f'{salario:.2f}')
print(f'{salario:.1f}')

#numero separados com milhar 
#a cada 3 casas ele coloca uma virgular 
print(f'{salario:,.2f}')

percentual = 0.1234
print(f'{percentual:.2%}')

#usando o format
print("{:.2f}".format(salario))

from decimal import Decimal

numero = Decimal("1234.54896")

#arredondar para 2 casas decimais 
print(round(numero,2))

valor = 1234.5
#formatando em forma de Moeda
print(f'R$ {valor:,.2f}')