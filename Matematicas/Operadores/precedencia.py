#precedendia é a ordem em que as operações São Realizadas
#ordem de Precedência dos operadores
# parênteses 
# potenciação
# multiplicação
# Divisão divisão inteiro e modulo
# soma
# subtração
#criando especificações pra dar 1024

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)

#calculadora imc
nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / (altura * altura)
print(f'Seu nome {nome} altura {altura} e seu peso {peso}')
print(f'Seu Imc é {imc:.1f}')

valor = 1000000
#dessa forma vou colocar os pontos e virgulas no valor 
print(f'{valor:,.2f}')