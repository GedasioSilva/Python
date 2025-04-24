def mostrar_lista(valor): #funcção recebe cada valor por vez da lista
    print(*list(valor),sep='\n') #cria outra lista e seprar
    print()

produtos = [
    {'nome': 'notbook', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'notbook 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'notbook 4', 'preco': 69.90},
]

encontrar_notbook = filter(
    lambda achou: achou['nome'] == 'notbook' , produtos
)
mostrar_lista(encontrar_notbook)