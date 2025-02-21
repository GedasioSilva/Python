#Manipulando chaves e valores em dicionarios
pessoa = {}

#dessa forma a variavel vai ter o nome do index 
#ai quando colocar ela no dicionario é como locar o 'nome'
chave = 'nome' 
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome']= 'Miranda' #criando uma chave e adicionando miranda
print(pessoa[chave]) #acessando a chave pelo nome da variavel

pessoa[chave] = 'Maria' #alterando o valor da chave
del pessoa['sobrenome'] #del é pra apagar a chave sobrenome

print(pessoa.get('sobrenome')) #nome pq não existe o sobrenome

#criar um if pra tentantar pegar o sobrenome que foi apagado o retorno é nome
#se o retorno for nome não existe se não pega pelo pessoa['sobrenome']
if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])    