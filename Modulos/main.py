import funcoes #importa todas as funções de uma vez podendo ficar pesado
from funcoes import somar,multi #dessa forma ele pega apenas a função especifica

somar() #importando de funções e pegando a função somar
funcoes.multi() #pegando por import
multi() #pegando pelo import a função multi


#puxa um modulo que ta dentro da pasta items

#ele não consegue achar arquivos dentro de pastas
#pra chamar funções dentro de uma pasta precisar criar uma index init e depois 
#utlizar essa forma pra chama a função dentro de cadastro no caso cliente
from items.cadastro import cliente
cliente()