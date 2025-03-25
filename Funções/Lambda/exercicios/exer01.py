#crie uma função lambda que aceite um número 
# é retorne o cubo desse numero

#pega o valor 5 que é x e faz ao cubo que são ** por 3
valor = 5
cubo = lambda x: x ** 3
print(cubo(valor))
'''
#multiplica o primeiro valor pelo segundo
x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))
multiplicador = lambda x,y: x * y
print(f'{x} vezes {y} é {multiplicador(x,y)}')
'''

#jogando os numeros da lista dentro da função lambda
#jogando cada index do numeros dentro do "x"
numeros = [1,2,3,4,5]
multiplicados = list(map(lambda x: x * 2 ,numeros))
print(multiplicados)

print(" ")
#verificando se é impar ou par
notas = [7,6,8,9]
somanotas = list(map(lambda x: x % 2 == 0,notas))
print(somanotas)

print(" ")
#Aplica uma função a todos os elementos de uma lista.

numeros2 = [1,2,3,4,5]
quadrados = list(map(lambda x: x ** 2,numeros2))
print(quadrados)

print(" ")
#Ordena uma lista de dicionários pelo valor da chave idade.

pessoas = [
     {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 20},
    {"nome": "Carlos", "idade": 30}
]

ordenado = sorted(pessoas,key=lambda x :x['idade'])
print(ordenado)