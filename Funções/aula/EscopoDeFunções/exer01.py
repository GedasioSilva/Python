x = 10
def mostar_global():
    print(x) #pode acessar , mas não pode modificar

mostar_global()

print(10*'---')
#agorar a funão vai poder modificar um valor da variavel global

def alterar_global():
    global x
    print(x  + 1)

alterar_global()

print(10*'---')

#Quando temos funções dentro de funções, podemos modificar variáveis do 
#escopo não global, mas sim da função que envolve.

def externa():
    mensagem = "Esse valor é da função externa"
    print(mensagem)

    def interna():
        nonlocal mensagem #Permite modificar a variável de "externa"
        mensagem = "Esse valor é da função interna"
        print(mensagem)

    interna()#executa a função interna
externa() #chama a função externa       