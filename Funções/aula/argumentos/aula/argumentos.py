#default = aquele que voce define o valor no parametro
#nom-Default Aquele que você não Define o valor No parametro
#o atributo que que já tem o valor definido de ser por ultimo no caso
#quantidade que tem o valor definido estar por último

def boas_vindas(nome,quantidade=6):
    print(f'Óla {(nome).capitalize()}')
    print(f'Temos {str(quantidade)} De Laptops em Estoque')
    
boas_vindas("dasio")

#tipos de funções realizam tarefas ou retornam valores

def cliente1(nome):#retorna só um valor na tela
    print(f'óla {nome}')


def cliente2(nome): #a função tem um valor porém não imprime na tela
    return f'Olá {nome}'


x = cliente1("Maria")#uma tarefa utilizar o print
y = cliente2("José") #se você quiser reutilizar utilizar o return

print(x)
print(y)

def imprimir(a,b,c):
    print(a,b,c)

imprimir(1,2,3)