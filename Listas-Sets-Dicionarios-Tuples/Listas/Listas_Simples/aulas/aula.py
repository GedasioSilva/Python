""" Definição lista
        Listas em Python
        Tipo list - Mutável
        Suporta vários valores de qualquer tipo
        Conhecimentos reutilizáveis - índices e fatiamento
        Métodos úteis: append, insert, pop, del, clear, extend, +
"""

string = 'ABCDE'  # 5 caracteres (len)

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria' #trocando no me de Luiz ótavio pra Maria
print(lista[3]) #chama toda a lista
print(lista[2], type(lista[2]))

print(10*"-",'SEPARANDO CONTEUDO',10*"-")

listaNome = ['Gedasio','Camila','Diana']

for nome in listaNome:
    print(nome)