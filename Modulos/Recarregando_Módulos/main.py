#pra conseguir recarrega o modulo outraz vezez  
import importlib 

#o módulo é singleton porque só pode 
# ser instancia uma vez no programa
import carregada
from carregada import variavel
print(variavel)

print(10*'-','SEPARANDO CONTEUDO',10*'-')
print(" ")
#pra conseguir chamar o módulo outras vezes usando o importlib

for i in range(3):
    importlib.reload(carregada)
    print(i,'\n') 