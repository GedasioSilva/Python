#extraindo valores da lista e convertendo em variaveis
""" Tira os pontos pra execução do programa
usuarionota = [] #uma lista vazia
notasUsuario = input("Informe as 4 notas sepradas por espaço: ").split()

for nota in notasUsuario:
    usuarionota.append(nota) #passando cada index pra lista usuarionota
    print(nota)

#print(*usuarionota) #mostrando toda a lista 

#agora vou pegar os index das notas do usuario e criar variaveis de 1 ate 4

#print(len(usuarionota)) pegando o tamanho da lista

print(type(usuarionota))

#a função retorna os index da lista usuarionota transformados em variaveis
def resultado(usuarionota):
    n1,n2,n3,n4 = usuarionota
    somanotas = n1 + n2 + n3 + n4
    return {somanotas}

print(resultado(usuarionota))

"""
print(" ")
print(30*"-",'SEPARANDO CONTEUDO')

pontos = [1,2,3,4,5] #lista com pontos
valormax3 = [] #lista vazia que vai receber pontos
for valor in pontos:
    if valor > 3: #condição
        valormax3.append(valor) #usando o append pra inserir valor

print(*valormax3) #desempacotando a lista

print(" ")
print(30*"-",'SEPARANDO CONTEUDO')

