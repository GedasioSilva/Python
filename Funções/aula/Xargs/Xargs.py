#Xargs é uma função onde seus argumentos não são definidos , podendo receber varios argumentos

def soma(*numeros):#com o * significa varios atributos
    resultado = 0 
    for num in numeros:
         resultado += num
    return resultado

    
x= soma(2,3,4,7,4)
print(x)

print(" ")

def agencia(**carro):#primeir "*" informa varios atributos segundoparametros
    return carro

print(agencia(marca ='Gol',cor ='Branca',motor = 1.0,placa = 1234))
print(agencia(marca ='Gol',cor ='azul',motor = 1.0))
print(agencia(marca ='palio',cor ='preto',motor = 1.0,placa = 1234))
