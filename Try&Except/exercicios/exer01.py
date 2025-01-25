#O tratamento de erros em Python é 
# feito principalmente usando o bloco try-except,
#  que permite capturar e lidar com exceções que podem
#  ocorrer durante a execução do código. Isso evita que
#  o programa termine abruptamente devido a erros não tratados.


try:#tenta executar o código
    numero = int(input("Digite um número inteiro: "))
    print(f"O dobro de {numero} é {numero * 2}.")
except ValueError: #se der erro vem para aqui
    print("Erro: Você deve digitar um número inteiro.")
else: #se não tiver error vem para essa parte
    print("Você digitou um número Valido")


try: #pede pra digitar um número
    numero3 = int(input("Digite um número: "))
except ValueError: #se não digitar vem aqui
    print(f'Error: você precisa digitar um número')    
else:#se digitar vai sair aqui
    print(f'O Número Digitado foi: {numero3}')    

