#peça pro usuario informa um número inteiro
numero = 9
#verificar se é inteiro ou não
if isinstance(numero,int):
    print("Número inteiro")
else:
    print("Número não inteiro")    

#verifica se é impar ou par 
if numero % 2 == 0:
    print('Número par')
else:
    print('Número impar')    


nome = input("Informe seu nome: ")
qtd = len(nome)
#verifica se o nome é longo ou não
if qtd >= 10:
    print("Nome é longo")
elif qtd >=5 and qtd <=9:
    print("Nome normal")
else:
    print("Nome pequeno")           
