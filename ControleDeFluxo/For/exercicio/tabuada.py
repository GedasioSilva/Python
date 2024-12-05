
numeroOperacao = int(input("Digite o Número da Tabuada:"))

for baseConta in range(1,11):
    print(baseConta , "x" , numeroOperacao ," == ", baseConta * numeroOperacao)
    
print("-------------------------------------------")    
    
  
for contador in range(0,11):
    print(contador , "+" ,numeroOperacao, "==" ,
        contador + numeroOperacao )
    
print("-------------------------------------------")    

for contador in range(0,11):
    print(contador , "-" ,numeroOperacao, "==" , contador - numeroOperacao )
 
print("-------------------------------------------")   
    
for contador in range(0,11):
    print(contador , "-" ,numeroOperacao, "/" , contador / numeroOperacao )               