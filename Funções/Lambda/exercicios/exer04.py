#verifica se o valor x e y são iguais
verifica = lambda x,y:x == y
print(verifica(10,9))

print("SEPARANDO CONTEUDO")

#retornando se x é impa ou par com uma lista
numeros = [1,2,3,4,5,6,7,8,9,10]
par_impar = list(map(lambda x: "Par" if x % 2 == 0 else "Impar",numeros))
print(par_impar)

print("SEPARANDO CONTEUDO")
#verifica se o é maior ou menor que o 7
notas = [7,6,5,7]
somanotas = list(map(lambda x: "Maior" if x >= 7 else "Menor",notas))
print(somanotas)

print(" ")

