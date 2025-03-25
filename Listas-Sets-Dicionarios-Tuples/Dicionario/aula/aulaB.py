#dicionario é utilizado pra adicionar coisas que tem atributo exemplo
##vou guardas carros só que esses carros tem valores ai cria um dicionario
#caso fosse guardar só o nome do carro usaria listas 

aluno = {
    'nome':'Ana',
    'idade':16,
    'nota_final':'A','Aprovacao':True ,
    'Materias':['Fisica','matematica','ingles']
} 

print(aluno)
#print(aluno.get('Materias')) #puxando as materias
#print(len(aluno)) #puxando o tamanho do dicionario
print(aluno.items()) #puxando items 
print(aluno.keys()) #puxando Keys
print(aluno.values()) #puxando Values

print(30*'-')

pessoa = {
    'nome':'Luiz Otávio',
    'sobrenome':'Miranda'
}
#outra forma de criar dicionarios com a função dict
pessoa2 = dict(nome='Luiz Otávio',sobrenome='Miranda')

#o loop roda e vai pegando os key e values da posição 0 
#pessoa.items() é o retorno
for key,values in pessoa.items():
    print(key,values)

print(30*'-')


pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

#acessando os items do dicionario
print(10*'-',"Separando Conteudo")
print(pessoa['nome'])

#utilizando o enumerate a chave começa no valor 1
for chave,valor in enumerate(pessoa,start=1):
    print(chave,valor)

print(30*'-')    