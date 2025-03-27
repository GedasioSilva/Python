"""
Utilizando o copy pra copiar os dados de uma lista pra outra
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() #usando o copy criar uma lista com os mesmo valores
#porem alterando a lista a não altera a lista B

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)