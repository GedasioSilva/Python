#else -> É uma cláusula opcional que executa um código se o código na cláusula try for executado sem lançar um erro 
#finally ->É uma cláusula que é executada em todos os casos 
#CRIANDO UM EXEMPLO SIMPLES COM ELSE E FINALLY
try:
    #mesmo sendo errado não vai cair no ValueError
    valor = int("100") 
except ValueError as e:
    #tenata mostra o Erro só que o código não deu Esse Error
    print(f"Erro: {e}") 
else:
    #se o código não tiver erro ai mostra o else
    print("Conversão bem-sucedida!") 
finally:
    #sempre vai ser executado
    print("Bloco finalizado.") 

print(10*'-')
print("Outro exemplo utilizando o else e o finally")
print(10*'-')

try:
    print('ABRIR O ARQUIVO')
    8/0 #criando um erro
except ZeroDivisionError as e: #colocando o erro com o apelido de 'e'
    print(e.__class__.__name__) #mostando o nome do erro
    print(e)#mostando o erro
    print('DIVIDIU POR ZERO')
except IndexError as error: #pegando o erro e criando um apelido
    print('IndexError')
except(NameError,ImportError): #como pegar dois erros por vez
    print('NameError','ImportErro')
else:
    print('Não Deu Erro') #se não tiver erro
finally:
    print('Sempre vai ser Executado')#executando de qualquer forma
