# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations,permutations,product

def print_iter(iterator): #a função criar uma lista com cada item 
    print(*list(iterator),sep='\n') #criando outra lista e separando ela
    print() #pular linha

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p','m']
]

#aqui separa os produto em ordem tipo camisetas tem preta do tamano p e m
print_iter(product(*camisetas))

print(10*"-",'Separando o conteúdo',10*"-")
#combinacão das pessoas em grupos de 2
#pegando os dados e criando grupos
print_iter(combinations(pessoas,2)) #chamando a função com combinations de pessoas com grupos de 2
print(10*"-",'Separando o conteúdo',10*"-")
print_iter(permutations(pessoas,2)) #a ordem não importa podendo ter ex joana e joao e joao e joana