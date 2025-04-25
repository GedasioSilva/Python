#Claro! A função reduce() em Python faz parte do módulo functools e é usada 
# para aplicar uma função a uma sequência de elementos, reduzindo-os a um único valor.


from functools import reduce
# reduce - faz a redução de um iteravel em um valor
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#o total é o acumulador
def funcao_do_reduce(acumulador,produto):
    print('acumulado' , acumulador)
    print('produto' , produto)
    print()
    return acumulador +  produto['preco']

#criando a função reduce
total = reduce(
    #primeiro uma funcao , segundo a lista 3 o valor inicial
    funcao_do_reduce,produtos,0
)
print(total)