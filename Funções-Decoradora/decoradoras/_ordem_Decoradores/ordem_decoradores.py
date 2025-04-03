#Ordem Dos Decoradores que se aplica de baixo pra cima

def parametros_decorador(nome): #o nome cai aqui 
    def decorador(func): #utilizo o decorador
        print('Decorador:',nome) #exibe o nome do decorador

        def sua_nova_funcao(*args,**kwargs):
            res = func(*args,**kwargs)
            final = f'{res} {nome}' #converteu o resultado pra string passaar o nome do decorador
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='segundo') #Passando um nome
@parametros_decorador(nome='primeiro') #Passando um nome
def soma(x,y):
    return x + y

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)