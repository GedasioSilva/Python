#Seus valores serão sempre unicos
#não aceitam valores mutáveis
#não tem index
#não garantem a ordem
#sao iteraveis (for , in , not in)

s1 = {1,2,3,3,3,4,5,1} #set com dados
print(s1)#remove valores duplicados

#print(s1[2]) não da certo porque não tem index

print(3 in s1) #perguntando se o 3 está no s1
for numero in s1: #mostando os números dentro do set
    print(numero)

#metodos para serem utilizados dentro do set

s2 = set()
s2.add('Gedasio') #adicionando
print(s2)
s2.update(('Camila','Diana')) #adicionando diversos valores
print(s2)
s2.discard('Camila') #eleminar o valor
print(s2)

