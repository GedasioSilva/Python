#convertendo os números
x = str(3) #colocando como string
y = int(4) #vai ser sempre int 
z = float(5) #vai ser sempre Float
w = 7.5


print(x + x) #string foi adicionado fica 33
print(y + y)  #fica 8 sem ponto  
print(z + z )  #fica 10.0 por causa do ponto flutuante


#o Andre tem 32 anos de idade e mora na cidade de São paulo

nome = 'Andre'
idade = 32
cidade = 'SãoPaulo'

print(' o ' + nome + ' tem ' + str(idade) + 'anos de idade e mora na cidade de ' + cidade)

print(int('1'),type(int('1'))) #convertendo pra int
print(type(float('1') + 1)) #convertendo pra float
print(str(11) + 'b') #convertendo pra String