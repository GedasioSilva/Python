#utilizamos o for quando sabemos quantas 
# vezes vai ser executado

for i in range(10):
    if i == 2:#verifica se i tem valor 2
        print('i é 2,Pulando...')
        continue

    if i == 8: #se i for 8 pausa o for
        print('i é 8,seu else não executará')
        break
    
    #não vai ser executado porque o loop foi parado no break
    for j in range(1,3): 
        print(i,j)
else:
    print('for completo com sucesso')    
