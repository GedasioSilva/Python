'''
Escopo significa o local onde aquele código pode atingir
Existe o escopo local e global
o escopo global é o escopo onde todo o código é alcançavel
'''
x = 1
def escopo():
    '''Variavel definida dentro da função'''
    x = 10 #esse x é dessa função tem valor 10
    print(x) #o x da função pai é 10
    def outra_funcao():
        x = 11 #esse x é dessa função tem valor 11
        y = 2
        print(x,y) #x dentro dessa função
    outra_funcao() #chamando a função ai executa a saida x e y
    

print(x) #x de fora da função
escopo()
print(x)


#alterando o valor da variavel global
g = 1

#dessa forma to passando o valor de 
# y para dentro da variavel global
def adicionar(y): 
    global g #estanciando a variavel com valor global
    g += y
    print(g)
adicionar(1)    