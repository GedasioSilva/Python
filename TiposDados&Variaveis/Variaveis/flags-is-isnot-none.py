#none criar uma varivale sem conteudo 
#flag é como se fosse uma bandeira pra marcar algo

# Exemplo de Flags e None
flag = True  # Flag como indicador
 
if flag is True:
    print("A flag está ativada.")
else:
    print("A flag está desativada.")
 
# Exemplo com None
nome = None
 
if nome is None:
    print("O nome ainda não foi definido.")
else:
    print("O nome é:", nome)

senhar = None #no caso a variavel esta vazia

#exercicio verifica se a senhar foi definida ou não
if senhar == None: #se for none mostra isso
    print('Senhar não informada')
elif senhar == senhar is not None: #se senhar não for not none é aqui
    print('Senhar informada')    