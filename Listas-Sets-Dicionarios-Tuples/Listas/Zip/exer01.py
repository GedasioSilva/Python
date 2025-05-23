# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#minha forma de juntar duas listas e mostrar em ordem alfabetica
cidades = ['Salvador','Ubatuba','Belo Horizonte']
estados = ['BA','SP','MG','RJ']

cidade_estados =zip(cidades,estados) #unindo duas listas

for cidade_estado in cidade_estados:
    print(sorted(cidade_estado)) #chamando as duas listas em ordem

print(10*'-','A Forma do Professor Responder',10*'-')

def zipper(lista1,lista2): #a função recebendo as Duas Listas
    intervalo_maximo = min(len(lista1),len(lista2))#mosta qual das duas tem o menor index
    return [ #não pode quebrar a linha no retorno
        #ta pegando o index da lista 1 e 2 até o valor maxino que é 3
       (lista1[i],lista2[i]) for i in range(intervalo_maximo) 
    ]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1,l2))  #a função passando as duas listas  