#filter é um filtro funcional

#a função pega um iteravel
def print_iter(iterator):
    #pega o iteral e transforma em uma lista
    print(*list(iterator),sep='\n')
    print()

#dicionario  
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#criar uma tupla com o metodo filter pra fazer validações
novos_produtos = filter(
    lambda p: p['preco'] >= 10 , produtos
)


#chamando a função
print_iter(produtos)
print("SEPARANDO O CONTEUDO")
print_iter(novos_produtos) #jogando o dicionario pra dentro da função