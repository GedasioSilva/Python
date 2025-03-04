#aula 173 caso de duvida

def gerador_aninhado():
    yield 1
    yield 2
    yield 3

def gerador_principal():
    yield 'A'
    yield from gerador_aninhado()  # delega a execução ao gerador aninhado
    yield 'B'

for valor in gerador_principal():
    print(valor)


#exemplo pra ir contando quando chegar no 7 mostra cr7

def cr7():
    yield ('Cristiano Ronaldo')

def primeira_parte():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield from cr7() #pra mostar cristiano ronaldo   chama a função cr7 
    yield 8 

for indice in primeira_parte():
    print(indice)

#a primeira tem 8 valores ai o indice vai adicionando 
# na posição 0 ate a 7 ai na sexta vai mostra a outra
#  função no caso cr7    