'''
A função all() em Python é uma função embutida usada para verificar se todos os elementos de um iterável (como listas, tuplas ou conjuntos) são avaliados como True. Ela retorna:

True: se todos os elementos do iterável forem verdadeiros ou se o iterável estiver vazio.
False: se pelo menos um elemento for avaliado como False.
'''

numeros = [1,2,3,4,5]
resultado = all(numeros)
print(resultado)

if resultado == True:
    print("Todos os dados da listas são Números")
else:
    print("Nem Todos os dados da lista são números")

#Com strings
print("Outra execursão de exemplo com all")

strings = ["Python","é","Legal"]
resultado2 = all(strings) #aqui verifica se todos são strings
valida = 'Verdadeiro ' if resultado2 == True else "Falso"      
print(valida)

print("Verifica se a condição é verdadeira ou falsa")
#Pelo menos um elemento falso
valores = [0, 1, 2, 3]
resultado4 = all(valores)
print(resultado4)  # Saída: False