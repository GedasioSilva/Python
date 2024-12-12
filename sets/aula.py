#similares a Listas
#evita itens duplicados
#não Utiliza index

list1 = [10,20,30,40,50]
list2 = [10,20,60,70]

num1 = set(list1) 
num2 = set(list2)

#operadores dentro set
print(num1 | num2 ) #operador | união dos sets tirando os valores repetidos
print(num1 - num2) #operador de diference os numeros que só tem em uma lista
print(num1 ^ num2) #symetric diference tira os duplicados das duas listas
print(num1 & num2) #and oque é duplicado em uma e na outra

print(len(num1)) #pega o tamanho da lista

print(" ")

#criando set
s1 = {1,2,3,4,5,6,6}
s1.add(7) #adicionando
s1.update([8,9,10,11]) #adiciona mais de um item
s1.remove(10) #removendo 
s1.discard(90) #discarata o número dando na listao ou não sem da Error
print(s1)

print(" ")

#Sets com strings

set1 = {'a','b','c'}
set2 = {'a','d','e'}
set3 = {'c','d','f'}

set4 = set1.union(set2) #união entre os sets
set4 = set1.difference(set3) #a diferença entre set1 e set2
set4 = set1.intersection(set2) #tem em ambos
set4 = set1.symmetric_difference(set3) #diferença cimetrica tira o duplicados
print(set4)