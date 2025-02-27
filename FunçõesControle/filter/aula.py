'''
A função filter() em Python é usada para filtrar
elementos de um iterável com base em uma condição, 
retornando apenas aqueles que atendem ao critério
definido por uma função.
'''
""" A função deve retornar True para os itens que devem ser mantidos.
    O iterável pode ser uma lista, tupla, conjunto, etc.
    O filter() retorna um objeto do tipo filter,
    então geralmente usamos list() para converter o resultado em uma lista.
"""
#filtando os items da lista que o resto por 2 fica zero
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 ==0 ,numeros))
print(pares)
print(" ")

#o list é pq criou uma lista pra sair o retorno
maiores_que_5 = list(filter(lambda x : x > 5 , numeros))
print(maiores_que_5)

print(" ")

pessoas = [
    {"nome": "Alice", "idade": 25},
    {"nome": "Bruno", "idade": 17},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Daniela", "idade": 16}
]

# Filtrar apenas os maiores de idade
maiores = list(filter(lambda pessoa: pessoa["idade"] >= 18, pessoas))
print(maiores)