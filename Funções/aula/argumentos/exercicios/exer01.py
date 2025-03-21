#criar uma função com valor de multiplicar definido

def multiplicar(valor,multiplicado=3):
    if valor == 0: #se o valor da variavel valor for zero
        print('valor invalido')
    else:
        resultado = multiplicado * valor
        print(resultado)
    return ' '


print(multiplicar(7)) #passando apenas um valor

print(10*'-','SEPARANDO CONTEUDO',10*'-')
print('\n')

#criar uma função onde o valor padrão é recife e se ela ta com
#o valor padrão ou o usuario informou algum outro valor
#verifica se ta usando o valor default ou não
def verifica(nome,estado = 'Recife'): 
    if estado == 'Recife':
        print('Valor padrão')
    else:
        print('Valor informado pelo Usuario') 

    return f' seu nome {nome} seu estado {estado}'

print(verifica('gedasio'))

print(20*'--')