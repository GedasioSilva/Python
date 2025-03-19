#Criar uma lista que recebe jogadores até chegar nos 5
#depois um for que mostra a lista com os valores recebidos e as posições 

qtd = 0
jogadores = []
while qtd < 5:
    valores = input("Insirar  Jogador da lista: ")
    jogadores.insert(qtd,valores)
    qtd += 1

print('\n')

tqd = 0
for jogador in jogadores:
    tqd +=1
    print(f'Posição do jogador: {tqd} Jogador {jogador}')

