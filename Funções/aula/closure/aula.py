'''
Closure é funções que retornam outras funções
'''
def criar_saudacao(saudacao,nome): #criar a função com 2 parametros
    def saudar():#criar outra função e executa ela esquecendo a primeira
        return f'{saudacao} , {nome}!'
    return saudar #o retorno da segunda função

#variavel recebe a primeira função onde passa os valores pra segunda função
s1 = criar_saudacao('bom dia','Luiz') 
s2 = criar_saudacao('boa Noite','Luiz')
print(s1())
print(s2())