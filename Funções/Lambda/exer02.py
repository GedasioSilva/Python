#Define uma função que retorna outra função lambda.

def multiplicador(n):
    return lambda x: x * n

dobro = multiplicador(2)
print(dobro(5))

print(" ")

def soma(m): #criando a função
    return lambda x: x * m #a lambda pega o x e multiplica por m 
    #o x ainda não foi definido o valor


numero = soma(3) #aqui ta adicionando o x
print(numero(5))
