pessoa = {'nome:':'Gedasio','idade':29}
pessoa['profissão'] = "Desenvolvedor" 
print(pessoa)

del pessoa['profissão']
print(pessoa)

#função dict pra criar usando variaveis
pessoa2 = dict(nome="joão",idade=27,cidade="Camaragibe")
print(pessoa2['nome'])

lista_pessoas = {'nome':['Camila','Diana','nubinha','Tieta','tino','bobo']}

#mostra os nomes das Pessoas
for nomes in lista_pessoas:
    print(lista_pessoas[nomes])

   