'''
crie uma lista de números de 1 a 10, se o numero atual for par imprima
se for impa imprima
'''
#a variavel numeros recebe uma lista com o range que conta vai ate 10
#indo de 1 e 1 até o limite 10
numeros = list(range(1,10))

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é Par")
    else:
        print(f'{numero} é Impar')    