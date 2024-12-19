#receber os dados e guardar em uma array
from array import array #importando o array

#crindo uma array
dados = array('i',[1,2,3,4,5,6,7,8,9,10])
print(dados[2])
#mostrando o index 3

dados.append(11) #adicionando
dados.remove(5) #removi o numero 5
#mostrando todos os index 
for numerosArray in dados:
    print(numerosArray)

print("Primeiro")

#
dados2 = array('i',[1,2,3,4,5])
for valores in dados2:
        quadrado =  valores * valores
        print(f'{valores} * {valores} == {quadrado}')

print("segundo")
#contar a quantidades de vezes que um número "1" aparece
#mostra quantas vezes o número não foi repitido
array3 = array('i',[1,2,3,4,1,6,7,1,9,1,1])
qtd = 0
nqtd = 0

for repitidos in array3:
    if repitidos == 1:
        qtd += 1
        print(f'o numero 1 foi Repetido {qtd} Vezes')
    else:
         nqtd += 1
         print(f'Número não repitido {repitidos}')    

print(" ")
print("Terceiro")
print(" ")

#soma valores inseridos no array e fazer a media entre eles

valoresinseridos = array('i',[7,3,3])
itensarray = len(valoresinseridos)

resultado = sum(valoresinseridos) / float(len(valoresinseridos))
print("O valor é {:.1f}".format(resultado)) #{:.1f} controla as casas decimais
#print( sum(valoresinseridos) / float(len(vetor)) ) [2]

print("Quarto")  

     
    

