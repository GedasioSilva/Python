''' Argues é quanto um função tem a entrada de dados indeterminada'''

#pegando os valores de args e somando
def nota(*args):
   total = 0
   for numero in args:
        print('Total',total,numero)
        total = total +  numero 
        print('Total',total)

nota(1,2,3,4,5,6)

print(" ")

def soma(*args):
    total = 0
    for numero in args:
        total += numero #dessa forma cada giro e conta numero com o numero do giro anterior
    return total #recebe o valor acumulado do for


soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

#usando a função sum
print(sum((1,3,2,4)))

print(" ")
''' Aqui estou passando uma tupla pra dentro da função
    e estou desempacotando os itens da tupla numeros
    Exemplo de argues recebendo um tupla e desempacotando os valores
'''
numeros = 1,2,3,4,5,6,7,8,9
outa_soma = soma(*numeros)
#pegando os itens da tupla numeros e separando eles 
print(outa_soma)


print(" ")
def contaNotas(*args):
    soma = 0
    for nota in args:
        soma += nota
    return soma / 4


resultado = contaNotas(7,8,9,6)
print(f'{resultado:.2f}') #retorno formatado com duas casa decimais



