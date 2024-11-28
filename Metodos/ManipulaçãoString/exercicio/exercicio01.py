#cortando as frases

frase = "olá da Gedasio"
print(frase[:6])#letras que vão se mostrada na frase
print(frase[-7:]) #as ultimas 7 letras

#letras maisusculas e menusculas
print(frase.upper()) #Maiusculos
print(frase.lower()) #menusculos
print(frase.title()) #primeira letra de cada palavra maiuscula
print(frase.capitalize()) #apenas a primeira letra Maiuscula

#trocando as Strings Gedasio por Camila
print(" ")
novaFrase = frase.replace("Gedasio","Camila")
print(novaFrase)


#Removendo e adicionando espaços
print(" ")
frase2 = " python "
print(frase2) #verdadeira forma
print(frase2.strip()) #remove espaços começo e fim
print(frase2.lstrip()) #adiciona espaço no fim 
print(frase2.rstrip()) #adiciona espaço no começo

# Dividir e Unir Strings
#separa a string em espaços
frase = "Python é incrível"
palavras = frase.split()
print(palavras)

#juntando as string
novaFrase = "-".join(palavras)
print(novaFrase)


#Checar se uma substring está presente.

frase = "Aprendendo Python"
print("Python" in frase)   # True
print("Java" not in frase) # True

