'''
Em Python, uma Higher Order Function (HOF)
é uma função que recebe uma função como argumento e/ou
retorna outra função como resultado.
Isso permite um código mais modular e reutilizável.
'''

def aplicar_operacao(funcao,valor):
    return funcao(valor)

def dobrar(numero):
    return numero * 2

def somar(numero):
    return numero + numero

print(aplicar_operacao(dobrar, 5))
print(aplicar_operacao(somar,2))

print(" ")

def converteSalario(ajuste,salario):
    return ajuste(salario)

def ajuste(valorpassado):
    return  valorpassado + 1

print(converteSalario(ajuste,100))

print(" ")

#criar uma função que recebe o valor das 4 notas
#a def dividemedia recebe a função medias e o valor passado
def dividemedia(medias,nota):
    return medias(nota)

def medias(notas):
    return notas / 4

print(dividemedia(medias,29))