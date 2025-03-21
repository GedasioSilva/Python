#O método split() em Python é usado para dividir uma string em partes, baseando-se em um delimitador especificado (ou espaço por padrão). Ele retorna uma lista com os pedaços resultantes. Aqui estão alguns exemplos de como utilizá-lo:

texto = "Python é incrível"
resultado = texto.split()
print(resultado)

for palavras in texto.split():
    print(palavras)


#slip tom tags de separar por "," é o maximo 
#já que o limite é 3 pq começo no 0 o três e quatro tao juntos
#separando a frase usando o enumerate
#curso professor otavio miranda

frase = "um , dois , três,quatro"
lista_frases_cruas = frase.split(',')

lista_frases = []
for i , frase in enumerate(lista_frases_cruas):
   lista_frases.append(lista_frases_cruas[i].strip())
print(lista_frases)
print("-----------------------------------")


#tirando as strings da frase e rodando no for
frase2 = "Meu  nome é gedasio"
palavras2 = frase2.split()
for frasess in frase2.split():
    print(frasess)

#join criar uma string vazia é onde é o atributo recebe a 
#forma que vai separar a string
#dentro dos aspas simples coloco oque vai serapar a frase
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

#posso utilizar o 
frase3 = ' '.join('abc')
print(frase3)