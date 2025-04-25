#reduce é utilizado apenas pra somar os valores
#importando o reduce  
from functools import reduce

numeros = [7,8,9,6]

#a lambda pega os valores x e y e soma , e os valores vem da lista número
soma = reduce(lambda x ,y: x + y , numeros)
if soma/4 > 7:
    print("Aprovado")
print(soma)

print("SEPARANDO O CONTEUDO")
print()

#lista que vou somar os valores
nome_sobrenome = ['gedasio','da','silva']

juntando_nome = reduce(lambda x , y: x + ' ' + y,nome_sobrenome).upper()
print(juntando_nome)
