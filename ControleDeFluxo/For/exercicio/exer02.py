#modificar de Fantastico para F A N T A S T I C O

palavra = input("Informe uma palavra que vai ser separada: ")

for spaco in palavra:
    print(spaco.upper() , end=' ') #end é que cada palavra continua na mesma linha sem pular e coloca espaço entre elas
    
    
#contar a quantidade de letras do seu nome 
nome = input("Digite seu nome:")
caracteres = len(nome) 
print(f'Seu nome tem: {caracteres} caracteres')    