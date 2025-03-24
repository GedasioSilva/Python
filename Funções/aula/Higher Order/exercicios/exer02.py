'''
Crie funções que duplicam , triplicam e quadruplicam
o número recebido como parâmetro
'''

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicadr = criar_multiplicador(2)
print(duplicadr(2))

triplicar = criar_multiplicador(3)
print(triplicar(3))

#outra forma de fazer o exercicio
