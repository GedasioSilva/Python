#criar um loop dentro do outro
qtd_linhas = 2 #quantidade de giros
qtd_colunas = 2 #quantidade giros

linha = 1
while linha <= qtd_linhas: #enquanto linha menor que qtd_linhas
    coluna = 1
    while coluna <= qtd_colunas: #outro loop enquanto coluna < qtdcoluna
        coluna += 1
        print(f'{linha=} , {coluna=}')
    linha += 1

print('acabou')
print(' ')

#exercicio 
nome = 'gedasio' #Iterâveis
contado = 0 #contador com o valor 0
novo_nome = ' ' #variavel vazia

while contado < len(nome): #condição
    letra = nome[contado] #letra recebe nome na posição contado
    novo_nome  += f'*{letra}' #novo nome += letra
    contado += 1 #contador
    
novo_nome += '*'
print(novo_nome)


    