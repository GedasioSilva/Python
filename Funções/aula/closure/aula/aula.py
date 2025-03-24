'''
Closure é funções que retornam outras funções
a função criar saudacao recebe saudacao e nome ai executa a saudar
só que a saudar não é executada ai só é executada quando print s1() é executado
'''
''' Definição
    Em Python, closures (funções fechadas) são funções internas que capturam e 
    lembram variáveis do escopo externo, mesmo após esse escopo ter sido encerrado.
    Elas são úteis para criar funções com estado.
'''
def criar_saudacao(saudacao,nome): #criar a função com 2 parametros
    def saudar():#criar outra função e executa ela esquecendo a primeira
        return f'{saudacao} , {nome}!'
    return saudar #o retorno da segunda função

#variavel recebe a primeira função onde passa os valores pra segunda função
s1 = criar_saudacao('bom dia','Luiz') #ele recebe os dados da função
s2 = criar_saudacao('boa Noite','Luiz')
print(s1())
print(s2())