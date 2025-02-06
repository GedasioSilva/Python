#quando for criar uma função é sempre com a palavra Def de definição
def boas_vindas():
    print("Olá Gedasio")
    print("Temos 5 lebtops em estoque")

#boas_vindas()

#função recebendo parametros
def somar_dois_numeros(n1,n2):
    numero1 = n1
    numero2 = n2
    resultado = numero1 + numero2
    print(f'A Soma de {numero1} + {numero2} é igual a {resultado}')    


#somar_dois_numeros(50,50)

print("----------------------------------------------------------")
#Parâmetros e Argumentos em uma função

def boas_vindas_argumento(nome,quantidade):
    print(f'olá {nome}')
    print(f'temos {str(quantidade)} laptops em estoque')

boas_vindas_argumento("gedasio",3)

''' Passando argumentos nomeados e não nomeados'''
def soma(x , y , z = None):
    if z is not None:
        ''' verifica ser z não for none'''
        print(f'{x=} {y=} {z=}',x+y+z)
    else:
        ''' se z for none sai essa saida de x e y'''
        print(f'{x=} {y=}' , x + y)    

#dessa forma passarmos os valores diretos para as variaveis
#dessa forma é parametro nomeado
#se passar o argumento nomeado todos os outro precisam ser nomeados
soma(x= 1 , y=4 , z = 0)

#verifica se foi passado algum valor pro z ou se é none
def valor(z=None,y = 0):
    if z is not None:
        print(f' não é none')
        print(f'o valor de Y é {y}')
    else:
        print(f' tem o valor none')    

valor(1)