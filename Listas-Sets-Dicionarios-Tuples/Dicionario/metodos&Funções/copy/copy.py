import copy
#copy é pra copiar os dados de um dicionario com outra
#importando o copy as copias são profundas pegando no segundo nivel


d1 = {
    'c1':1,
    'c2':2,
    'li':[0,1,2]
}
#utilizando o copy ele copia os items
#caso atualizar os d2 não mexe no d1
d2 = d1.copy() #d2 copia o d1 
d2['c1'] = 1000 #alterando o valor de c1 no dicionario 2
#se alterar em outro nível como uma lista dentro da outra
d2['li'][1] = 99 
print(d1)
print(d2)

print(10*'-','  COPIAS SIMPLES',10*'-')
#exercitando
notasgedasio =[7,8,9,7] #notas do aluno gedasio
notascamila = notasgedasio.copy()

#aqui a lista notas camila copiou as notas da lista notasgedasio
#vou alterar a nota no index 3

for nota in notascamila:
    print(nota)

print(10*'-','  COPIAS COMPOSTAS',10*'-')

notasnubia = {
    'notas':[8,8,7,9],
    'final':8
}

notasdiana = copy.deepcopy(notasnubia)
#alterando em uma altera na outras
notasdiana['notas'][3] = 8
print(notasdiana)
print(notasnubia)


