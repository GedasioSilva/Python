'''
forma de economizar uma grande contidade de linhas de código
<valor> if <condição> else <outro valor>
''' 
idade = 16
resultado = 'Voto Permitido' if idade >= 16 else 'voto não permitido'
print(resultado)

salario = 1600
resposta = 'salario minimo' if salario < 1450 else 'Não é salario minimo'
print(resposta)

vaga = False
requesito = 'desenvolvedor php' if vaga == True else 'Não é programador'
print(requesito)

condicao = 10 == 10
variavel = condicao if True else 'Outro Valor'
print(variavel)

#se o digito for maior que nove o digito vira zero se ele for menor fica ele mesmo

digito = 10
'''verifica se o digito é maior que 9 ou não se for ele vira 0'''
novo_digito = digito if digito <= 9 else 0
print(novo_digito)