#Exercitando combinações produtos e permutations

from itertools import combinations,permutations,product

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

carros = [
        ['opala','gol','uno'],
        ['verde','branca','vermelhor']
    ]


#combinations -> pega o valor e combina sem repetir
print(list(combinations(carros,2)),sep='\n')
print(list(combinations(pessoas,2)))

#permutations combina de todas as formas possiveis 
print(*list(permutations(carros,2)),sep=' ')
