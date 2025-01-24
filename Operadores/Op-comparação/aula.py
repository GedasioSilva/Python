#Os operadores relacionais em Python são usados para comparar valores. Eles sempre retornam um valor booleano: True (verdadeiro) ou False (falso).
#Tabela de operadores Relacionais
# == Igualdade
# != diferente
# > maior que
# < menor que
# >= maior igual
# <= menor igual

x = 10 
y = 20
print(x == y) #false 
print(x != y) #true pq é diferente

print("----------------------------")

a = 15
b = 10
print(a > b) #true
print(a < b) #false
print(a >= b) #true
print(a <= b) #false

print("----------------------------")

#comprarando Strings
nome1 = "Alice"
nome2 = "bob"
print(nome1 == nome2) #false
print(nome1 < nome2) #true nome1 começa com a nome2 começa com B

print("----------------------------")
#comprando com variaveis diferentes

x = 5
y = "5"
print (x == y) #false

print("----------------------------")

#uso combinado com condicionais

# idade = int(input("Digite sua Idade: "))
# if idade >= 18:
#     print("você é maior de Idade: ")
# else:
#     print("você não é Maior de idade: ")
    
#comparações complexas
x = 10
print(x > 5 and x < 20) #true
z = 3
print (not(z == 10)) #true
print("----------------------------")
y = 10
u = "10"
print(y == int(u))

#outros exemplos de operadores de comparação
print("Outros Exemplos")

maior = 2 > 1
print(maior)
menor = 1 < 2 #1 é menor que 2
print (menor)
menor_ou_igual = 2 <= 2 #é igual a 2 ou menor
print(menor_ou_igual)
igual = 'a' == 'a' #igual 
print(igual)
diferente = 'a' != 'b' #diferente
print(diferente)
