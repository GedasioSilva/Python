#criar uma promoção do produto de 100 reais 
#depois ir baixando o valor do produto
import random

valor = 100
dia = 1
#ver se o valor é maior que 20 depois imprime o valor depois tira 5 do valor

while valor > 20:
    print(f'O dia é: {dia} o produto vai ser vendido por: R$:{valor}')
    dia += 1
    valor -=5 
    

numero_sorteado = random.randint(1,10)
tentativas = 7
desistir = None

print("Sorteio da Mega Sena digite seu numero:")
print("Você tem 7 tentativas Boa Sorte")

while tentativas > 7:
    numero = int(input("Informe o Número sorteado de 1 até 10: "))
    if numero < 0 and numero > 10:
        print("Número sorteado Invalido")
        break
    
    if numero == numero_sorteado:
        print("Você Acertou o número sorteado Parabéns!!")
        break

    if numero != numero_sorteado:
        print("Você errou é Perdeu uma tentativa: ")
        numero = int(input("Informe o Número sorteado de 1 até 10: "))
        tentativas -= 1


