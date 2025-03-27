'''
datanascimento = input("Data nascimento: ")
if isinstance(datanascimento,int) == True:
    print("Dado informado valido")
else:
    print("Dado Invalido")

    
valorCamisa = float(input("Valor da camisa: "))
if isinstance(valorCamisa,float) == True:
    print("Dado informado Valido")
else:
    print("Dado Invalido")


nome = input("Informe seu nome: ")
if isinstance(nome,str) == True:
    print("Dado informado Valido")
else:
    print("Dado Invalido")  
                
'''
validaIdade = input("Voce é maior de idade: ")

if validaIdade == "sim":
    validacao = True
else:
    validacao = False
    print("Error")
    
       
if isinstance(validacao,bool):
    print("Resposta  verdadeira")
else: 
    print("Resposta  falsa")    







