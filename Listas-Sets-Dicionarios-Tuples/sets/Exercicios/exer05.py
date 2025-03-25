#vou criar um set com 10 e vou ver se os 5 sorteados estão nele
import random #importando o random

numeros = set() #criando o set de numeros 
numeros.update([3,4,6,8,7]) #numeros escolhidos usuario
sorteados = set() #onde vai receber os números da random
verificasorteado = set()


for valor in range(5):
    valor = random.randint(1,10)
    sorteados.add(valor)


verificasorteado = numeros.intersection(sorteados)


if len(verificasorteado) > 1:
    print("Parabéns")
    print(*verificasorteado) #os números que o usuario acertou 
else:
    print("Você perdeu")    
