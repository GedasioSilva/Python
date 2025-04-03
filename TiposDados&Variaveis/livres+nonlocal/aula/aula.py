#uma variavel é considerada livre dentro de um função quando a
#variavel não é definida no escopo interno da função 

""" 
#variaveis livres + nonocal (locals,globals)
#print(globals()) #pega todas as variaveis de definidas globalmente

def fora(x):
        a = x # o a é livre pq não é uma variavel que recebe dados
    def dentro():
        return a # o a no escopo dentro da def mãe
    return dentro #retornando a propria função

    dentro1 = fora(10)
    print(dentro1())
"""

def concatenar(string_inicial):
    valor_final = string_inicial #valor final recebe a string

    def interna(valor_a_concatenar):
        #valor final que no caso é o valor a que vem da primeira função
        nonlocal valor_final #o python cria como se a variavel fosse definida nessa função
        #variavel que não é dessa função só pode pegar o valor atribuido e não pode alterar ela
        valor_final += valor_a_concatenar
        return valor_final 
    return interna

#o c ta recebendo a função e ta passando um valor pra função concatena
c = concatenar('a') 
print(c('b'))
print(c('c'))
print(c('d'))