
#inserindo numeros em uma lista pra depois fazer a soma com sum
qtdDividas = int(input("Informe quantas dividas você tem: "))
numeros = []

for i in range(qtdDividas):
    numero = int(input("Digite os valores das suas dividas: "))
    numeros.append(numero) 

print('Os valores das suas Dividas: ',sum(numeros))


#agora usar um input pra inserir os numeros e depois verificar o maior

entrada = input("Digite números separados por espaço: ")
valores = list(map(int,entrada.split()))
print(max(valores)) # pegando o maior valor 
print(min(valores)) #pegando o menor valor
