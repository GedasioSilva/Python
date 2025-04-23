#Aplica uma função a cada elemento e retorna 
#um novo iterável com os resultados

def triplica(numero):
    return numero * 3

numeros = [1,2,3,4,5]
resultado_map = map(triplica,numeros)

print(list(resultado_map))

print("SEPARANDO O CONTEUDO")
print(" ")

#adicionando mais 1
def adicionar(nota):
    return nota + 1

notas = [7,6,8,4,5]
notas_maps = map(adicionar,notas)
print(list(notas_maps))

print("SEPARANDO O CONTEUDO")
print(" ")

numeros2 = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2 , numeros2))
print(dobrados)

print("SEPARANDO O CONTEUDO")
print(" ")

nomes = ['ana', 'bruno', 'carlos']
maiusculos = list(map(str.upper, nomes))
print(maiusculos)
