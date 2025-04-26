def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n - 1)

print(fatorial(5))  # Saída: 120
print(fatorial(3))  # Saída: 6

print("SEPARANDO O CONTEUDO")
print()

#vou criar uma função que vai diminuindo o valor até chegar a zero

def diminuir(valor):
    if valor == 0 or valor == 1:
        return 1
    #fica rechamando ae atende alguma condição de cima    
    return f'{diminuir(valor - 1)} Diminuindo.... '
    
print(diminuir(3))

print("SEPARANDO O CONTEUDO")
print()

def fibonnacci(n):
   if n <= 1:
       return n
   return fibonnacci(n -1 ) + fibonnacci(n-2)
print(fibonnacci(2))