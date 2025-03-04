#Em Python, funções geradoras (ou generator functions)
# são funções especiais que permitem produzir uma 
# sequência de valores ao longo do tempo, em vez de 
# retornar todos os valores de uma vez. Elas utilizam 
# a palavra-chave yield em vez de return.

#a função vai chamando até aparecer o 
# yield ai pausa e espera ser chamanda denovo

def genetator(n=0): #a função receber o valor
    yield 1 #mostra o retorno e Pausa
    print('continuando...')
    yield 2 #Pausar na proxima chamada da função
    print('Mais uma vez...')
    yield 3 
    print('Vou terminar')
    return 'Acabou'

gen = genetator(n=0)

for n in gen:
    print(n)


    