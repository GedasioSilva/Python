#empacotamento e desempacotamento de dicionarios
pessoa = {
    'nome':'aline',
    'sobrenome':'Souza'
}
a,b = pessoa.values()
#no caso a e b estão pegando os valores dentros dos index do dicionario
#a esta recbendo o item dentro da posição 0 nome o 0 que é aline
print(a,b)

#empacotando
dados_pessoa = {
    'idade':16,
    'altura':1.6
}

pessoa_completa = {**pessoa,**dados_pessoa} #passando os dados de pessoa pra pessoa completa
print(pessoa_completa)

#monstando todos os dados que foram passados pro dicionario pessoa completa
for chave,valor in pessoa_completa.items():
    print(chave,valor)

