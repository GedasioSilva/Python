'''
#tuples é uma lista só que com forma de escrita e armazenamento são diferente
#a tubles não pode alterar e remover os dados
#se precisar criar uma lista muito grande use toples ou que o itens não serão alterados
Tuplas não podem ser mudadas
'''
cores_list = ['amarelo','verde','azul','vermelho']
cores_tuplues = ('amarelo','verde','azul','vermelho')

print(type(cores_list)) #lista
print(type(cores_tuplues)) #tuple

nomes = 'Maria','Helena','Luiz'
print(nomes[1])

#converter de listas para Tuples
cores = ['amarelo','verde','azul','vermelho']
cores_tuple = tuple(cores) #pegando a lista e tranfomando em tupla

#convertendo pra listas denovo
cores_lista = list(cores_tuple)