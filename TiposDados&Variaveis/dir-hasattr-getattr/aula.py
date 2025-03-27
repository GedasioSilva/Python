#utilizamos pra verificar se existe um metodo dentro da string
# dir verifica se o metodo esta dentro da string
# hasattr verificar se a string tem um atributo
# getattr pega o atributo
#aula 144

string = 'Luiz'
print(dir(string),'\n') #verificando os metodos 
metodo = 'upper'

print(10*"",'SEPARANDO CONTEUDO')
print(" ")

if hasattr(string,'upper'): #verifica se tem o metodo upper na string
    print('Existe Upper')
    print(getattr(string,metodo)()) #chamando a variavel metodo que tem Upper
else:
    print('Não existe o Método' , metodo)

print(" ")
print(10*"",'SEPARANDO CONTEUDO')
print(" ")

baixo = 'lower'
#getattr pega o metodo já que o 
#conteudo da variavle baixo e lower ai chama o metodo
print(getattr(string,baixo)())    