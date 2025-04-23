'''
    GeneratorType é o tipo (classe) dos objetos geradores 
    criados por funções com yield Ele faz parte do módulo types.
'''
from types import GeneratorType

# Função geradora
def contador():
    yield 1
    yield 2
    yield 3

# Criando o gerador
gen = contador()

# Verificando o tipo
print(isinstance(gen, GeneratorType))  # True
print(type(gen))                       # <class 'generator'>


