#Mapeamento de dados em list comprehension (map)
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    #produto a chave pegano o preco e adicionando 1.05 no valor
    {**produto , 'preco':produto['preco'] * 1.05 }
    for produto in produtos]#pegando apenas os nomes

print(*novos_produtos, sep='\n') #pra desempacota a lista e adicinar a quebra de linha com '\n'

#retornando se os números forem maior que 3
numeros = [1,2,3,4,5,6]
maiores = [x for x in numeros if x >= 3]
print(maiores)

#colocando os nomes em maiusculos
nomes = ['ana','bruno','carlos']
upper = [nome.upper() for nome in nomes]
print(upper,'\n')