#main é sempreo modulo principal onde vou 
# chamar os importes de outros modulos

from sys import path

import conteudo.conteudo
from conteudo.conteudo import bemvindo,adeus,variavel
#importando a pasta com os  modulo especificos

#from conteudo.conteudo import *
#importando com todos os conteudos 
#porem o professor informa que foi má pratica

#criei um loop que pede pra informa que chega ou sai
while True:
    cheque = input("Chegando [1] ou saindo [2] ..")

    if cheque == '1': #verifica se chega se sim
        print(bemvindo()) #imprime a função que vem do módulo
        break
    elif cheque == '2': #imprime a função que vem do módulo
        print(adeus())
        break
    else:#se não entende continua perguntando ate ser chegando ou saindo
        print("Não entendi pode Repetir")
        cheque = input("Chegando ou saindo..")

#    print(__name__)#assim a pessoa verifica qual o modulo principal
#    print(*path , sep='/n')
print(variavel)