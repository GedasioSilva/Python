#são forma de criar index nas listas 
#criando uma lista enumerada caso uma lista com o index
#enumerate ele enumera cada item da lista

lista = ['Maria','Camila']

#dessa forma eu pego o index e o nome
for indece,nome in enumerate(lista):
    print(indece,nome) #já cria a lista com enumerador no caso "0 Maria"

print(" ")
print(15*"-",'SEPARANDO CONTEUDO',15*"-")

#criar uma lista de nomes com o enumerate
#dessa forma cria uma lista com os index
lista_nomes = ['Gedasio','Diana','Camila']
#enumerando a lista começando do 1
for item in enumerate(lista_nomes,start=1):
    print(item)

