#Tipos de dados str = "estring" 
# int = "inteiro" float = "Flutuante"
#Tipo Boleano

#tipos Strings 
nome2 = 'Gedasio'
nome = "Gedasio"
print(type(nome))
print(type(nome2))


#Tipos floats 
numeroInteiro = 10
print(type(numeroInteiro))

#Tipos floats
numeroFlutuante = 7.9
print(type(numeroFlutuante))

valores = numeroInteiro + numeroFlutuante
print("{:.1f}".format(valores))

#Tipo de Dados boleanos recebe os valores como True e False

print(10 == 10) #true
print(10 == 11) #false

condicao = False
if condicao == False:
    print("Valor não aceito")
else:
    print("Valor Aceito")    
print(condicao)

condicao2 = True
if condicao2:
    print("Verdadeiro")
else:
    print("Falso")    

