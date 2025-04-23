#exercicio pra ordenar os lutadores por ranks
from itertools import groupby

lutadores = [ #uma classe de lutadores
    {'nome': 'Anderson Silva', 'rank': 'A'},
    {'nome': 'Poatan', 'rank': 'B'},
    {'nome': 'Aldo', 'rank': 'A'},
    {'nome': 'Charles', 'rank': 'C'},
    {'nome': 'Ruffy', 'rank': 'D'},
]

#uma função pra ordenar a lista pelo index rank
def ordena(lutador):
    return lutador['rank']

#a lista lutador fazendo uma copia rasa com sorted
lutador_agrupado = sorted(lutadores,key=ordena)

grupos = groupby(lutador_agrupado,key=ordena)

#o for pega a chave e o nome da lista grupos 
#cada lutador vai ser pego toda vez que o for rodar dentro da lista grupos

for chave , nome in grupos:
    print(chave)
    for lutador in nome:
        print(lutador)