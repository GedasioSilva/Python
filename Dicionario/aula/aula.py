#Dicionarios 
    #utiliza index em formato de Keys e Values
    #aceita string, integer , float , bolean...

#criando dicionario    
aluno = {'nome':'Ana','idade':16,'nota_final':'A','Aprovacao':True} 
print(aluno['nome'],['idade'])

#atualizar o nome
aluno['nome'] = 'Gedasio' #atualizando o nome
print(aluno['nome'])    #mostrando o nome atualizado

aluno.update({'idade':'28','nota_final':'B'}) #alterando os dados com update