numeros = [2,3,4,5]
letras = ['a','b','c']

numeros.extend(letras) #pegando números e estendendo com letras
#final = numeros + letras
#final = numeros * 2 #imprimindo as litas 2 vezes
print(numeros)

print(" ")
#criando uma lista dentro de outra
#quando divide cada conjunto de dados dentro do [] vira um index
itens = [['item1','item2'],['item3','item4']]
print(itens[0]) #itens da posição zero item1 e item2
print(itens[0][1]) #itens da posição 0 do index 1 item2

print(" ")
valores = [50,80,110,150,170]
for x in valores:
    print(F'O valor final do Produto é: {x}')
    

print(" ")
#Verificando itens em uma lista
cores = ['amarelo','verde','azul','vermelhor']
cor = input("Digite a cor que deseja: ").lower()

if cor in cores:
    print('temos essa cor em Estoque')
else:
    print("Não temos essa cor em Estoque")


#trabalhando com lista dentro de lista

salas = [
    ['Maria','Helena'],
    ['Elaine'],
    ['Luiz','João','Eduarda',(0,10,20,30,40)]
]
print(salas[2][2]) #buscando o index Eduarda
print(salas[2][3][2])#buscando na linha 3 o index 4 valor 2
#no caso o retorno é o 20

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)