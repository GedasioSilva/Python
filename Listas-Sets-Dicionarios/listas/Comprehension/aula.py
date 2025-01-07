
#list comprehension
    #Mais simples de escrever
    #util quando você precisa criar uma nova lista apartir de uma existente
    #expressao for item in itensi
    
#pegar as frutas onde o nome tem a letra B    
frutas1 = ['banana','manga','goiaba','morango','abacaxi']  
''' 
frutas2 = []

for iten in frutas1: #girar a lista 
    if 'm' in iten: #verificar se o nome da fruta tem a letra B
        frutas2.append(iten) #append pra adicionar os iten em frutas2   
        
print(frutas2)
''' 
#primeiro iten for iten é ora rodar
#in frutas1 if b in item é pra verificar se em frutas tem a letra b
#o iten é pra mostra os iten que tem a letra b 
frutas2 = [iten for iten in frutas1 if 'm' in iten]

print(frutas2)    