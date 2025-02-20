'''
Nessa aula função como argumento de outra função
aula 114
'''
#a função que recebe uma mensagem e nome
def saudacao(msg,nome):
    return f'{msg},{nome}' #retorna a mensage e nome

def executa(funcao,*args): #executa recee a função saudacao e diversos argumentos
    return funcao(*args) #aqui mostra a saudacao recebe diversos argumentos

print(
    executa(saudacao,'bom dia','Gedasio')
)