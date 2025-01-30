#Listas 
# Armazena mais de uma informações em variaveis
# manter a sequencia dos dados em uma variavel

cidade1 = "Rio"
cidade2 = "janeiro"
cidade3 = "SaoPaulo"

cidades = ['Rio de janeiro','São Paulo','Salvador']

cidades[0] = "Recife" #colocando o item 0 como recife    

numeros = [1,2,3,4]
print(numeros)


print(" ")
print("Append")
##append(): Adiciona  "um" elemento ao final da lista.
cidades.append('Santa catarina')
print(cidades)

print(" ")
print("Remove")
#remove(): Remove a primeira ocorrência de um valor.
#remove a primeira vez que o 5 for encontrado

cidades.remove('Salvador')
print(cidades)

print(" ")
print("Inserte")
#insert(): Insere um elemento em uma posição específica.
cidades.insert(1,'Rio Grande do sul')
print(cidades)


print(" ")
print("pop")
#pop remove o último porém mostra oque foi removido
#retirando o último elemento  da lista
#se você não passar o index o pop deleta o último 
print(cidades.pop()) #mostrando oque foi removido

print(" ")
print("sort")
#organizar em ordem alfabetica
cidades.sort()
print(cidades)

print(" ")
print("Extendes")
#extend(): Adiciona múltiplos elementos de outra lista ou iterável.
cidades.extend(['Maceio','Jaboatão'])
print(cidades)

#clear é pra limprar a lista apagando os registros
#cidades.clear()

for cidade in cidades:
    print(cidade)