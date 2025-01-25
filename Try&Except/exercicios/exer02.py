try:
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    resultado = numerador / denominador
    print(f'o Resultado é: {resultado:.2f}')
except ZeroDivisionError: #codigo do error 
    print(f"Error: Não é Possivel dividir por Zero: ")
except ValueError:
    print("Erro: por favor, insira Apenas Números inteiros.")        

#index fora do intervalo
try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Erro: Índice fora do intervalo.")


try:
    numero3 = int(input("Digite um número: "))
except ValueError:
    print("Erro: valor Inválido")
else:
    print(f'Você digitou: {numero3}')        
