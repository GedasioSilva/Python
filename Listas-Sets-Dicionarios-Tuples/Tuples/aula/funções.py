"""
    Tuples (ou tuplas) em Python são sequências imutáveis,
    usadas para armazenar múltiplos itens em uma única variável.
    Aqui estão algumas funções e métodos úteis para trabalhar
    com tuplas:
"""

tupla = (1,2,3,4,5) #criando a tupla
print(len(tupla)) #pegando o tamanho da tupla
print(15*'-','SEPARANDO O CONTEUDO')
print(max(tupla)) #pegando o maior valor no caso 5
print(15*'-','SEPARANDO O CONTEUDO')
print(min(tupla)) #pegando o menor 1
print(15*'-','SEPARANDO O CONTEUDO')
print(sum(tupla)) #pegando todos os valores 15
print(15*'-','SEPARANDO O CONTEUDO')
print(tupla.count(1)) #conta quantas vezes o valor 1 aparace
print(15*'-','SEPARANDO O CONTEUDO')
print(tupla.index(5)) #mostra em qual index o valor aparece primeiro


print(15*'-','SEPARANDO O CONTEUDO')
print("Fatiamento de Tuplas")
tupla = (10, 20, 30, 40, 50)
print(tupla[1:4])   # (20, 30, 40)
print(tupla[:3])    # (10, 20, 30)
print(tupla[::2])   # (10, 30, 50)

print(15*'-','SEPARANDO O CONTEUDO')
print('Verificando se um Elemento Existe')
tupla = (10, 20, 30)
print(20 in tupla)   # True
print(50 not in tupla)  # True