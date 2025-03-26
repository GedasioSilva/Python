#exercitando o kwargs argumentos nomeados
#o kargs retorna um dicionario 

def pessoa(**kargs):
    for chave,valor in kargs.items():
        print(chave,valor)

#inserindo diversos valores nomeados
pessoa(nome='gedasio',idade=29)

print(10*"-",'SEPARANDO O CONTEUDO')

#vou criar uma função que recebe dados e fazem a validação
def funcsenhar(**kargs): #recebendo o kargs
    for chave,valor in kargs.items(): #pegando a penas o valor
        senhar = valor #passando o valor pra senhar
    #verificando se a senhar é valida ou não
    retorno = "confirmada" if senhar == 123 else "Invalida" 
    print(retorno)
   
funcsenhar(senhar=123)

print(10*"-",'SEPARANDO O CONTEUDO')
print(" ")
#passando kwargs para outra função
def mostrar_dados(nome,idade):
    print(f'Seu nome: {nome} sua idade: {idade}')

dados = {"nome":"Gedasio","idade":29}
mostrar_dados(**dados)    