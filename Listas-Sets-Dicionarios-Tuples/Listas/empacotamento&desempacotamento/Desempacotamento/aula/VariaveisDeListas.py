print("Extraindo variaveis de listas")
#Extraindo variáveis de Listas
produtos = ['Arroz','Feijão','Laranja','banana']
item1 ,item2 , item3 ,*outros = produtos #variaveis recebendo os index
#tipo a lista produtos tem 4 itens eu tenho 3 variaveis a que sobra fica
#em outros se sobrar mais de uma fica em outros e outros vira uma lista
print(item1)
print(item2)
print(item3)
print(outros)

print(" ")
#tirando os index e criando variaveis
nomes = ['Gedasio','Camila','Diana']
nome1,nome2,nome3 = nomes
print(nome1,nome2)

#passando os valores das variveis a primeira recebe o 7 
# e a nota2 recebe todos os outros valores
#se não quiser os valores restantes use o '*_'
notas = [7,8,9,10]
nota1,*restoValores = notas
print(nota1,restoValores)

#dessa forma vamos pular a segunda nota que eu não quero pegar o valor
notasemestre = [8,9,10]
primeiranota,*_,terceiranota = notasemestre
print(primeiranota,terceiranota)

#outra forma de pula um elemento e pegar apenas os escolhidos
#desempacotamento em chamadas 
#de métodos e funções

lista = ['Maria','Helena',1,2,3,'Eduarda']

#dessa forma eu pego os index maria helena 
# pulo os números e pego Eduarda na última variavel
p,b,*_,u = lista
print(p,b,u)