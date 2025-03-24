#vou criar uma função que tem outras duas 
#funções que são retirar e adicionar o 
#closure vai salvar o salto e as outras funções vão fazer as operações


def saldoconta():
    saldo = 1500 #valor definido na função principal

    #dessa forma a função deposito pode mexer no escopo externo
    def sacar(valor): #o valor passado é recebido aquie e tratado nessa função
        nonlocal saldo
        sacado = saldo - valor
        return f'O SEU SALDO: R${sacado}'
    return sacar #retorna a função inter

sacarvalor = saldoconta()
print(sacarvalor(1300)) 

def conta(): #função principal
    valordepositado = 1300 #valor da função principal

    def depositar(valor):#recebe um valor 
        nonlocal valordepositado #pega o valor da função pai
        saldo = valordepositado + valor #calculo
        return f'O SEU DINHEIRO EM CONTA É {saldo}' #saida
    return depositar #essa função salvar o valor porem não retorna

valorpradepositar = conta()
#o valor de 700 passa pra função conta que é tratado pela função
#depositar que pegar o valor da função pai valordepositado e adiciona com o valor
#que foi passado no caso o valor 700 ao retorno fica 2000
print(valorpradepositar(700)) #aqui o valor é passado e a funcao depositar é executada

      