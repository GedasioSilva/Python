#exercitando o empacotamento 
#recebendo valores e fazendo as somas

def valores(*args):
    total = 0
    for numero in args:
        total = total + numero
        print(f'{numero} a soma do número {total}')

valores(1,2,3,4,5)

#criar uma função com as notas das 4 unidades se 
#for lançado mais de 4 notas aceita apenas as 4 primeiras

print(15*'-','SEPARANDO O CONTEUDO')

def notas(*args): #args por pradrão é uma tupla
    somavalores = sum(args[0:3]) #recebendo apenas os valores de 0 até 4
    media = somavalores / 4
    print(f'{media:.1f}') #saida com apenas uma casa decimal

notas(7,6,8,9,9)

print(15*'-','SEPARANDO O CONTEUDO')
#criar uma função que recebe diversos valores e mostrar os inpas e par

def impar():
    return 'impar'

def par():
    return 'Par'

def dados(*args):
    for valor in args:
        if valor % 2 == 0:
            print(par(),valor)
        else:
            print(impar(),valor)

dados(1,2,3,4,5,6,7,8,9,10)        