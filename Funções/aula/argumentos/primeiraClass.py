'''
Nessa aula função como argumento de outra função
aula 114
'''

def saudacao(msg,nome):
    return f'{msg},{nome}'

def executa(funcao,*args):
    return funcao(*args)

print(
    executa(saudacao,'bom dia','Gedasio')
)