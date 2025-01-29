import random

numero_sorteado = random.randint(1,10)
tentativas = 7

print("Sorteio da Mega Sena digite seu numero:")
print("Você tem 7 tentativas Boa Sorte")

while tentativas > 0:
    numero = int(input("Informe o Número sorteado de 1 até 10: "))

    if numero > 10:
        print("Número sorteado Invalido")
        numero = int(input("Os numeros são de  1 até 10: "))
        continue
    elif numero == numero_sorteado:
        print("Você Acertou o número sorteado Parabéns!!")
        break
    elif numero != numero_sorteado:
        print("Você errou é Perdeu uma tentativa: ")
        print(f'{tentativas} Menos 1' )
        numero = int(input("Informe o Número sorteado de 1 até 10: "))
        print(f'Sua tentativas {tentativas}')
        tentativas -= 1


