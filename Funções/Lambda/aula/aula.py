#função Lambda
    #é uma função pequena sem nome
    #pode ter varios argumentos mas somente 1 expressao
    #Muito Utilizada dentro de outras funções
    #Código mais 'clean'
    
def soma(x):
    return x + 10 
    #return criar como se fosse uma variavel pra guradar o valor

print(soma(1))

somar10 = lambda x,y: x + y + 10 #criando a função
print(somar10(2,3)) #atribuindo o valor pra dentro de lambda

print(" ")
#lambda dentro de outra função

def somar(x):
    func2 = lambda x:x + 4 #recbe o valor dentro da função soma
    return func2(x) * 4 #multiplica o valor que foi passado por 4

print(somar(2))



