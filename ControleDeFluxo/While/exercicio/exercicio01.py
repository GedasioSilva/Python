'''
Escreva um programa em Python que use um loop while para pedir ao usuário um número.
O programa deve continuar pedindo números até que o usuário digite um número maior que 10.
Quando isso acontecer, o programa deve exibir uma mensagem dizendo que o número é válido e encerrar.
'''
numero = int(input("informe um numero: "))
while numero < 10:
    numero = int(input("continue informando um número: "))

#consultar senhar
#ir adicionando na media até ela seja menor ou igual a 7
media = 5
while media <= 7:
    print("Media ainda é menor: " , media )  
    media = media + 1
    continue 


contador = 0
while contador <= 10:
    contador += 1
    contador = 8 #se contador chear em 8 acabou
    print(contador)
    break

print('acabou')    