#exercitando funções Geradora
#funções Geradoras vai executando aos poucos e fica parando
#esperando next pra executar outra coisa

def contador():
    for i in range(5):
        yield i

#Cada chamada de next(gen) avança para o próximo valor.
gen = contador()
print(next(gen))
print(next(gen))
print(next(gen))

print(10*'-',"SEPARANDO O CONTEUDO",10*'-')

#cada vez que a função for executada com o nex o
# salario aumenta 3 porcento
def aumento_salario():
    salario = 1500
    while True:
        yield f'{salario:.2f}'
        salario += salario /100 * 0.3 #passando o aumento

aumento = aumento_salario()
'''
print(next(aumento))#executando a função       
print(next(aumento))#recebendo o primeiro aumento
'''
#fazendo um for que executa a função aumento_salario 10 *
for contador in range(10):    
    print(f'{contador} {next(aumento)}')


print(10*'-',"SEPARANDO O CONTEUDO",10*'-')

#fazer uma função que tem o valor 3 
#cada vez que executar o valor é diminuido

def contador_execucao():
    contador = 3
    while contador > 0:
        yield contador
        contador = contador - 1

subitraindo = contador_execucao()
print(next(subitraindo))        
print(next(subitraindo))        
print(next(subitraindo))        
       