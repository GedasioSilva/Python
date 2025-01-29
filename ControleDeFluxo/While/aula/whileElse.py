#Usando While com else

string = 'valorqualquer'

i=0
while i < len(string):
    letra = string[i]

    if letra == '':
        break
    print(letra)
    i += 1
else:
    print('Não Encontrei o espaço na String')
print('Fora do While. ')

