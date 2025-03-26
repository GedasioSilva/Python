#Dictionary Comprehension e Set Comprehension
produto = {
    'nome':'caneta Azul',
    'preco':2.5,
    'categoria':'Escritório'
}

dc = {
    chave:valor.upper() #passando a chave e valor a chave sendo uppercase
    if isinstance(valor,(int , float)) else valor #isinstance verifica se valor é str se não coloca só o valor
    for chave , valor 
    in produto.items() #retornando os items
    if chave != 'categoria' #se o if for diferente de categoria
}
print(dc)