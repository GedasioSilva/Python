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

print(" ")    
#como o for funciona
#iteralve -> str rang ,etc (_iter_)
#iterador -> quem sae entregar um valor por vez
#next -> entrega  o proximo valor 
#iter -> me entregue seu iterador

#string é o iteral
texto = iter('Luiz') #_iter_()  
print(texto.__next__()) #entregar o primeiro item da string
print(next(texto)) #entregar o segundo item da string
print(texto.__next__()) #entregar o segundo item da string
print(next(texto)) #entregar o segundo item da string

#se chamar mais que a contidade de itens da error
#isso aqui mostra como o for funciona

iterador = iter(texto) #iterator

while True: #while infinito esperando uma condição pra parar
    try: #tente executar
        letra = next(iterador) #vai chamar o proximo intem da variavel
        print(letra) #vai mostra o proximo item da string
    except StopIteration: #verifica se dar esse error se der
        break #pare o sistema    