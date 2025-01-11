#informa se o numero é pá ou não
numero = 19

if numero % 2 == 0:
    print("Par")
else:
    print("Impar") 
    
#outro exercicio pedir um número au usuario se for maior que 10 encerrar
contador = 0
numero_informado = int(input("Informe um Número: "))
if numero_informado > 10:
    print("O número é um valor valido")
else:
    while numero_informado < 10:
        contador += 1
        numero_informado = int(input("Informe outro número pra verificar:"))
        if numero_informado >= 10:
            print(f"parabéns número valido e custou: {contador} tentativas")    