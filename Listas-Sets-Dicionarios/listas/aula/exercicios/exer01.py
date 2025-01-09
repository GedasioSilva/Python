#criar uma lista de frutas e imprimir os items da lista
frutas = ['maça','banana','manga','uva']
for fruta in frutas:
    print(f'Fruta: {fruta}')

#contar os elementos da lista
qtd = len(frutas)
print(qtd)

#imprimir o primeiro e o último elemento da lista
print(f'A primeira Fruta é {frutas[0]}')
print(f' A última fruta é {frutas[-1]}')#menos 1 conta de traz pra frente

frutas[1] = 'morango' #frutas no index 1 adiciona morango
frutas[0] = 'pera' #adicina na posição 0 a pera
frutas.append("abacaxi") #inserir um item no final da lista
print(frutas)

for fruta in frutas:
    print(f'Frutas no seu carrinho de comprar:  {fruta}')

print(" ")

lista_nomes = [''] #criar uma lista vazia
lista_nomes[1:3] = ['Gedasio','Camila']
#adicionar nas posição de 1 até 3 no caso vai na 1 e na 2
print(lista_nomes)
lista_nomes.insert(0,'Diana') #vou inserir no index 0
lista_nomes.insert(1,'Núbinha') #vou inserir no index 0
print(lista_nomes[0:3]) #pegando de 0 até 2

#removendo nomes da lista
lista_nomes.remove('Diana') #removeu Diana o index 0
print(lista_nomes)
del lista_nomes[-1] #excluir o último item da lista
print(lista_nomes)


