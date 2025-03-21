#Listas dentro de outras listas 
#buscando os valores de uma lista dentro da outra

salas = [
    ['Maria','Helena'],
    ['Elaine'],
    ['Luiz','João','Eduarda',
    (0,10,20,30,40)]
]
print(salas[2][2]) #buscando o index Eduarda
print(salas[2][3][2])#buscando na linha 3 o index 4 valor 2
#no caso o retorno é o 20

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

print("SEPARANDO O CONTEUDO")
#pegando apenas os index da lista sala na coluna 3 (0 10 20 30 40)
qtd = 0
total = 0
while qtd < 5:
    print(salas[2][3][qtd])
    qtd += 1



