#Agregando Duas listas com o Zip

cores = ['amarelo','verde','azul','vermelhor']
valores = [10,20,30,40]

duaslistas = zip(cores,valores)
print(list(duaslistas))

print(" ")

#pega uma string e divide como se fosse um array
var = list('dasio')
print(var)

print(" ")

lista = [123,True,'Luiz Otavio',1.2]
lista[2] = 'Gedasio'
for item in lista: #PEGANDO OS INDEX DA LISTA
    print(item)


#cuidados com dados mutáveis
#aponta para o mesmo valor na memória
#no caso quando eu apontar tipo lista b recebe o mesmo valor da lista a
#se caso um valor foi atualizado na lista a vai mudar nas duas listas

lista_a = ['Maria','Luiz']
lista_b = lista_a 
lista_c = lista_a.copy()
#utilizando o copy no caso pegar os dados da lista e coloca em outra 
#mesmo atualizando a lista a não via mudar os dados da lista C

lista_a[0] = 'Qualquer valor'
print(lista_b)
print(lista_c)


