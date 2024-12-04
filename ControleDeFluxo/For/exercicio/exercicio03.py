#criar um retangulo com a saida output do terminal

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas): #vai rodar 6 vezes
    for c in range(colunas):
        print(simbolo , end='')
    print()#ele roda a o primeiro loop quando acaba as 6 vezes ele pula uma linha    