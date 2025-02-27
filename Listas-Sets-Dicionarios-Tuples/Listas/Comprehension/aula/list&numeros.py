valores = []

for x in range(6):
    valores.append(x * 10)
    
print(valores)


#dentro de uma list comprehension
#vai fazer o x vezes 10 dentro do for rodando 6 vezes 
valores2 = [x * 10 for x in range(6)]
print(valores2)

#criar uma lista compreheison com mais de 1 for

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y)) #tupla com x e y

#to fazendo da index x e y pra rodar dentro de um for onde eles ficam recebendo valores
lista = [ 
    (x,y) 
    for x in range(3) #o 3 vai receber 3 valores
    for y in range(3) #o y vai receber 3 valores
]        
print(lista)