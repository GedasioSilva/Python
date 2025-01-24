#O tratamento de erros em Python é 
# feito principalmente usando o bloco try-except,
#  que permite capturar e lidar com exceções que podem
#  ocorrer durante a execução do código. Isso evita que
#  o programa termine abruptamente devido a erros não tratados.

try:
    numero = int(input("Digite um número inteiro: "))
    print(f"O dobro de {numero} é {numero * 2}.")
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")



    