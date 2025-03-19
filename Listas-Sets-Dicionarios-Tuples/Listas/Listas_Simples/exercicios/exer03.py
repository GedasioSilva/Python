#o exercicio é criar formas de mostrar o valor da lista junto com o index

lista =['Maria','Helena','luiza']

itens = len(lista)
contador = 0

while contador < itens:
    for nome in lista:
        print(contador ,nome)
        contador += 1

print(" ")

indeces = range(len(lista))
for indece in indeces:
    print(indece,lista[indece])
    
print(" ")

valores = len(lista) #contar o tamanho da lista
index = 0 #contador em 0

while index < valores: #enquanto contador fo menor que valor contador +1
    print(index,lista[index])
    index += 1
