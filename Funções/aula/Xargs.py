#Xargs é uma função onde seus argumentos não são definidos , podendo receber varios argumentos

def soma(*numeros):#com o * significa varios atributos
   for num in numeros:
        resultado += num
    return resultado  
x = soma(2,3,4,7)
print(x)