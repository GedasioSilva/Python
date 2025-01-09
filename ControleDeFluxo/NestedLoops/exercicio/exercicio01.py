filhos = ('Camila','João','Xênia')
funcionario = ('zefinha','biu')

for numero in range(2):
    print('Nome do Funcionario:' , funcionario[numero])
    for numero2 in range(3):
        print(filhos[numero2])

#fazer o for loop de notas dos aluno cada aluno tem 4 notas
alunos = ['gedasio','camila']
notas = [7,6,5,9]

print(" ")

for aluno in alunos:
    print(f'Nome do Aluno: {aluno}')
    for nota in notas:
        print(f'Suas Notas: {nota}')


frutas = ['maça','banana','manga']
vegetais = ['cenoura','alface','brocolis']

for fruta in frutas:
    for vegetal in vegetais:
        print(f'A Fruta {fruta} O vegetal {vegetal}')