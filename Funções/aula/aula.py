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
