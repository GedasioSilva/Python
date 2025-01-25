#tratamento de Erros caso o valor se invalidado é jogado em ValueError onde output o retorno
#Erros
    #Excelente para testes
    #Não Realiza o 'Stop' no programa
    #Mensagens customizadas quando encontrar um Erro

#Trabalhando com o Try e Except com o input
try:
    valor = int(input("Digite Um valor: "))
    print(valor)
except ValueError:
    print("Porfavor, insira um valor Válido: ")
else:
    print('Usuario digitou um valor correto')
    conta = valor * 2 / 100 #pegar 0 juros
    resultado = valor + conta #somar o juros no valor
    print(f'o valor final com o juros:{resultado}') #postar o valor com juros
        

#quando der um erro o sistema mostrar o erro ai pegamos o error e colocamos dentro do except


      
                 

