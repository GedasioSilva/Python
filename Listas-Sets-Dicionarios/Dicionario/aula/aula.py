#Dicionarios 
    #utiliza index em formato de Keys e Values
    #aceita string, integer , float , bolean...

#criando dicionario    
aluno = {'nome':'Ana','idade':16,'nota_final':'A','Aprovacao':True} 

#atualizar o nome
aluno['nome'] = 'Gedasio' #atualizando o nome
#print(aluno['nome'])    #mostrando o nome atualizado

aluno.update({'idade':'28','nota_final':'B'}) #alterando os dados com update


#aluno.update({'endereco':'Rua A'})#se não tiver o campo ele cria
#print(aluno.get('endereco','não existe'))

#del aluno['idade'] #removendo o campo idade
#print(aluno)

#aluno.keys() mostra os index
#aluno.values() mostra os valores
#aluno.items() mostra index e valores
for keys,values in aluno.items():
    print(keys , values)
    
       