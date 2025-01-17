numeros = [1,2,3,4,5,6]

#vai retorna os quadrados dos numeros da lista
quadrado = lambda x : x ** 2
resultado = []

#pegar a lista resultado e adiciona a função que recebe o numero
# esse numero vai ser o x da lambda onde o x é multiplicado por ele mesmo

for numero in numeros:
    resultado.append(quadrado(numero))

print(resultado)        