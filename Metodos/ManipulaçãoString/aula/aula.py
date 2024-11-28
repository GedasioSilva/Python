linguagem = 'python'
nome = 'GEDASIO'
frase = ' Python e uma boa linguagem'


#converter a string para letras nimuscula
print(nome.lower())

#convertendo a String para Maisculo
print(linguagem.upper())

#Remove espaços em branco (ou caracteres específicos) do início e fim.
print(frase.strip())

#replace(): Substitui partes da string.
print(frase.replace("Python" , "PHP"))

#Deixa a primeira letra em maiusculo
print(linguagem.capitalize())

#procura por uma letra ou uma palavra informa a posição
print(frase.find('b'))

#posso procurar a onde inicia a palavra "linguagem" inicia na 18
#se a palavra não for encontrada retorna menos 1 (-1)
print(frase.find('linguagem'))


#len(): Retorna o tamanho de um objeto (string, lista, dicionário, etc.).
print(len([1, 2, 3]))  # Saída: 3

#enumerate(): Retorna índices e valores de um iterável.
for i, v in enumerate(["a", "b"]):
    print(i, v)
# Saída: 
# 0 a
# 1 b

#zip(): Combina elementos de iteráveis em pares.
lista1 = [1, 2]
lista2 = ["a", "b"]
print(list(zip(lista1, lista2)))  # Saída: [(1, 'a'), (2, 'b')]
