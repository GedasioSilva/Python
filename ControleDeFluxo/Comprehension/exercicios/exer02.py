#criar uma função que recebe os dados por  kwargs e mostra com list comprehension

def mostrar_dados(**kwargs):
    return [f'{chave}:{valor}' for chave,valor in kwargs.items()]

lista_dados = mostrar_dados(nome='gedasio',idade=29)
print(lista_dados)
        
print('SEPARANDO O CONTEUDO')
print()

def alunos_aprovados(*args):#recebendo diversos dados de entrada 
    nome_alurnos =  [nome for nome in args]
    print(nome_alurnos)

aprovados = alunos_aprovados('gedasio','camila','bitito')
aprovados

