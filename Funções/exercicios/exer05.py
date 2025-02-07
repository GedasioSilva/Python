'''
Crie uma Função que Multiplica todos os argumentos 
não nomeados recebidos da variavel
'''
'''
    pega o argumento e multiplica ele por ele mesmo 
    e mostra o retorno em cada loop
'''
def multiplica(*args): #args é uma tupla
    for numero in args:
        resultado = numero * numero
        print(f'Multiplicar {numero} por {numero} Dar: {resultado}')

multiplica(0,1,2,3,4,5)

print(" ")

''' 
    A função recebe o número e informa se ele é Par ou impar
'''

def par(numero):
    if numero % 2 == 0:
        print(f'O {numero} é Par:')
    else:
        print(f'O {numero} é impar')

numero = 3
par(numero)