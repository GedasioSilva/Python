# For Loops {Looping}
#rang informa quantas vezes vai ser chamado
#inicio no caso 1 até 20 de 2 e 2
#para em 19 pq o proximo loop passa de 20 fica 21 

for numero in range(1,10,2):
    print(numero)
    
print(" ")
#utilizar For Loops para String

palavra = 'Espetacular'
for letra in palavra: #dessa forma imprime letra por letra
    print(f'{letra} Esta dentro da Palavra {palavra}')
    