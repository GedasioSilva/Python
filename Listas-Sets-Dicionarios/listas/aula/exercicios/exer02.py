#fazer uma lista pra contar quantas vezes aparece o nome maça

lista_frutas = ['manga','maça','goiaba','maça','morango','maça']

qtd = 0
for fruta in lista_frutas:
    if fruta == 'maça':
        qtd += 1
        print(f'Outra maça: {qtd}')
    print(fruta)
       
#verificar se tem a moto no estoque
estoque = ['fan','titan','start']
pesquisa_moto = str(input("Informe qual a moto escolhida: "))

if pesquisa_moto in estoque:
    print("Temos a moto")
else:
    print("Não temos a moto escolhida: ")    

#notas recebe uma lista com 4 elementos
notas = list(range(4))
numero = 3
#o if verifica se tem o numero em notas
if numero in notas:
    print("temos esse número")
else:
    print("Não temos esse Número")    
