#Empacotamento e desempacotamento de dicionários 
# + *args e **kwargs

#a, b = 1, 2 criar duas variaveis que recebem 2 valores
# print(a, b) #exibindo

#empacotamento de um dicionario
#desse forma to pegando os dados de 
#um dicionario e jogando em variaveis
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

(a1,a2),(b1,b2) = pessoa.items()
print(a1,a2)
print(b1,b2)

print(10*"-",'SEPARANDO CONTEUDO')
print(" ")
#dessa forma eu estou pegando a chave e valor de pessoa
#desempacotar e tirar coisas de dentro do dicionario
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

for chave, valor in pessoa.items():
    print(chave, valor)

print(10*"-",'SEPARANDO CONTEUDO')
print(" ")

#pegar os dados de dois dicionarios e juntar
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa2 = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

#quando utilizo 2 ** é pra extrair os dados de um dicionario
pessoas_completa = {**pessoa2, **dados_pessoa}
print(pessoas_completa)

print(10*"-",'SEPARANDO CONTEUDO')
print(" ")

