#Try , except , finally Aula 174 caso duvidas futuras
#try não pega erros de sintax

try: #tenta executar o programa
    a = 18
    b = 0
    print(b[0])
    print(b == list)
    c = a / b
except ZeroDivisionError: 
#Esse erro é se caso a variavel b seja dividida por 0
    print('Dividiu por zero.')
except NameError:
#esse erro é se a varivael b não for definida    
    print('Nome b não está definido')
except TypeError:
    print("Aqui pega os Type erro ")    
except Exception:
    #aqui não pega um erro expecifico apenas informa que teve um erro
    print('ERRO DESCONHECIDO.')

print('CONTINUAR') #condinua depois que verifica se caiu em algum erro
