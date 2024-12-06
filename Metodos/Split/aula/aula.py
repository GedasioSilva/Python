#O método split() em Python é usado para dividir uma string em partes, baseando-se em um delimitador especificado (ou espaço por padrão). Ele retorna uma lista com os pedaços resultantes. Aqui estão alguns exemplos de como utilizá-lo:

texto = "Python é incrível"
resultado = texto.split()
print(resultado)

for palavras in texto.split():
    print(palavras)


#slip tom tags de separar por "," é o maximo 
#já que o limite é 3 pq começo no 0 o três e quatro tao juntos

frase = "um , dois , três,quatro"
resposta = frase.split(" , ",2)
print(resposta)