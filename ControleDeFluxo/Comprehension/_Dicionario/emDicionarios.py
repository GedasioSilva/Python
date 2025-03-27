#Dictionary Comprehension e Set Comprehension
produto = {
    'nome':'caneta Azul',
    'preco':2.5,
    'categoria':'Escritório'
}

dc = {
    chave:valor #passando a chave e valor a chave sendo uppercase
    if isinstance(valor,(int , float)) else valor #isinstance verifica se valor é str se não coloca só o valor
    for chave , valor 
    in produto.items() #retornando os items
    if chave != 'categoria' #se o if for diferente de categoria
}
print(dc)

print("SEPARANDO O CONTEUDO")
print(" ")

#Alterar os dados do dicionario com comprehension
#Modificando valores de um dicionário existente
precos = {'maçã': 2.50, 'banana': 1.50, 'laranja': 3.00}

desconto = {
    fruta: preco * 0.9 
    for fruta, preco in precos.items()
}

print(desconto)  
# Saída: {'maçã': 2.25, 'banana': 1.35, 'laranja': 2.7}
