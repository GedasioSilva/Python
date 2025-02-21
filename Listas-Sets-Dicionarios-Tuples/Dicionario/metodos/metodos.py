# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

''' Agora vou criar exemplos simples dos metodos'''

pessoa = {
    'nome':'Luiz Otávio',
    'sobrenome':'Miranda',
}
print(len(pessoa)) #conta quantas chaves tem 
print(pessoa.keys()) #retorna as chaves
print(pessoa.values()) #pegando os valores
print(pessoa.items()) #pegando chaves e valores
pessoa.setdefault('idade',0) #cria a key idade com valor padrão
'''
verifica se idade tem o valor padrão ou não
if pessoa['idade'] == 0:
    print('idadse padrão')
else:
    print('idade não padrão')    
'''

#for pegando as chaves e valores
for chave,valor in pessoa.items():
    print(chave,valor)

#copy é pra copiar os dados de um dicionario com outra
d1 = {
    'c1':1,
    'c2':2,
    'li':[0,1,2]
}
d2 = d1.copy() #d2 copia o d1 
d2['c1'] = 1000 
print(d1)
print(d2)

print(10*'-')
#com o get a pessoa pega o valor especifico
print(pessoa.get('nome')) #pegando diretamente pelo get 

print(30*'-')

p1 = {
    'nome':'Luiz Otávio',
    'sobrenome':'Miranda'
}
'''
pop ele pega os dado de p1 nome e depois apaga
nome = p1.pop('nome') 
print(nome) retornando o nome 
print(p1) apaga o nome em p1

#apagar a ultima chave do dicionario
ultima_chave  = p1.popitem()
print(ultima_chave) #faz a chamanda de oque foi apagado no caso sobrenome
print(p1)#chamando os items de p1 e so retorna nome pois sobrenome foi apagado
'''
#update atualiza os items que eu fo especificando
#e também cria outra chave
p1.update({
    'nome':'Gedasio',
    'sobrenome':'Silva',
    'idade':29
})
print(p1)

#outra forma de utilizar o update para atualiza os dados
p1.update(nome='Camila' , sobrenome='candida')
print(p1)

