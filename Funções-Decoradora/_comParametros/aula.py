#Decoradores com Parâmetros
#aula 192

def decoradora(func): #recebendo a função soma
    print('Decoradora 1')

    #cria um função interna
    def aninhada(*args,**kwargs):
        print('aninhada')
        res = func(*args,**kwargs)
        return res
    return aninhada #retorna a função interna

@decoradora
def soma(x,y):
    return x + y

multiplica = decoradora(lambda x, y: x * y)
dez_vezes_cinco = multiplica(10,5)
print(dez_vezes_cinco)

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)