# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
#Utilizando o raise pra da o retorno que eu escolher pra especificar o erro

#a função que não aceita se o valor passado for zero
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True #mostrando que foi passado o zero


def deve_ser_int_ou_float(n):
    tipo_n = type(n) #verifica o tipo 
    #aqui verifica se o dado de entrada e int ou float
    if not isinstance(n, (float, int)): 
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.' #pegando o  nome
        )
    return True


def divide(n, d): 
    deve_ser_int_ou_float(n) #verificando se o n é int ou float
    deve_ser_int_ou_float(d) #verificando se o d é int ou float
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))