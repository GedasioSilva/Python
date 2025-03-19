#útilizamos tuplas quando os valores passados pra 
#ela não devem e não podem ser atualizado

nomes = ('Gedasio','Camila','Diana','núbia')
idades = (31,29,8,3)

#concatenando os valors das duas tuplas
nomes_idades = nomes + idades
print(nomes_idades)

ordenados = sorted(idades,reverse=True) #ordenando do maior pro menor
print(tuple(ordenados))

print(" ")
print(15*"-",'SEPARANDO CONTEUDO',15*"-")

#verificar se tem determinador valor dentro de uma tupla
#to pegando apenas o valor Gedasio da tupla nomes
nomeGedasio , *outros = nomes
print(nomeGedasio) 

if nomeGedasio in nomes:
    print(f"Tem o valor {nomeGedasio} na tupla")
else:
    print("Não tem o valor Gedasio")

print(" ")
print(15*"-",'SEPARANDO CONTEUDO',15*"-")

#verificando se tem os numeros 
numerosEscolhidos = 3,2
numeroSorteados = (1,2,3,4,7,5,6,8,9)

print(sum(numeroSorteados)) #a soma dos números sorteados

if numerosEscolhidos[0] and numerosEscolhidos[1] in numeroSorteados:
    print("Tem os numeros ")
else:
    print("Não tem os Números")    