#criar uma lista de notas e copyar a lista de notas do primeiro aluno

#aui o aluno 1 ta recebendo as notas
aluno1_nota = [7,8,9,5]

#aqui o aluno 2 ta copiando as notas do aluno1
aluno2_nota = aluno1_nota.copy()
print(aluno2_nota)

#fazendo a soma das notas do aluno 2
mediaAluno2 = sum(aluno2_nota)
print(mediaAluno2)#mostando o resultado da soma das notas

print(10*'-','SEPARANDO O CÓDIGO',10*'-')

#aqui o aluno 1 ta trocando o valor da primeira nota pra 9
aluno1_nota[0] = 9 
mediaAluno1 = sum(aluno1_nota) #somando os valores da nota
print(mediaAluno1) #mostrando

#verificando os valores das notas do aluno 1
for valores in aluno1_nota:
    print(valores)


#por ser uma copia os valores passados pro aluno2 não são alterados
# quando a primeira nota do aluno 1 é alterada por isso o retorno do valor são 
# diferentes    


