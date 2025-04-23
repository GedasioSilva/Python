'''
    Boa! O partial em Python é um recurso muito legal da biblioteca 
    functools que permite pré-definir alguns argumentos de uma função. 
    Isso é ótimo pra simplificar funções que você chama repetidamente 
    com alguns argumentos fixos.
'''

from functools import partial


def potencia(base , expoente):
    return base ** expoente

# Cria uma nova função que sempre usa expoente 2
#partial defini o argumento expoente com valor fixo
quadrado = partial(potencia , expoente=2 )
print(quadrado(4))

print("SEPARANDO O CONTEUDO")
print(" ")

binario = partial(int,base=2)
print(binario('1010'))