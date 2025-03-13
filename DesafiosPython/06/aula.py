# Exercício - Adiando execução de funções
def soma(x, y): #criando a função soma
    return x + y


def multiplica(x, y):#criando a função multiplica
    return x * y


def criar_funcao(funcao,x):
    def interna(y):
        return funcao(x,y)
    return interna

#soma recebe criar um funcao que recebe a função soma
soma_com_cinco = criar_funcao(soma, 5) 
#multiplica_por_dez recebe criar um funcao que recebe a função multiplica
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))

