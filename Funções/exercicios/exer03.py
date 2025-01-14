#função recursiva onde o valor de entrada é passada por uma condição
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    
user_number = 5
print(f' o fatoria de {user_number} é {fatorial(user_number)}')    

#função recursiva onde o valor de entrada é passada por uma condição
def sorteado(numero):
    if numero == 0:
        return "codigo invalido"
    elif numero > 0 or numero < 10:
        return "codigo valido" 

usuario= 1348
print(f'{usuario} O seu código é {sorteado(usuario)}')

#função recursiva onde o valor de entrada é passada por uma condição

def fibonacci(n1):
    if n1 == 0:
        return 0
    elif n1 == 1:
        return 1
    else:
        #aqui roda um loope onde faz n1 menos 1
        #depois n2 - 2
        return fibonacci(n1 - 1) + fibonacci(n1 - 2)
    
termo = 7
print(f'O {termo} número da sequencia de fibonacci é {fibonacci(termo)}')

