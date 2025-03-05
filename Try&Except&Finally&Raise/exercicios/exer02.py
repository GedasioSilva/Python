
try: #tratando erro de divisão por Zero
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    resultado = numerador / denominador
    print(f'o Resultado é: {resultado:.2f}')
except ZeroDivisionError: #codigo do error 
    print(f"Error: Não é Possivel dividir por Zero: ")
except ValueError:
    print("Erro: por favor, insira Apenas Números inteiros.")        

print(10*'-')

#tratando erro de fora do intervalor
try:#pegando o errow porque o index 5 não tem na lista
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Erro: Índice fora do intervalo.")


print(10*'-')

try:#pegando erro se não for passado um int
    numero3 = int(input("Digite um número: "))
except ValueError:
    print("Erro: valor Inválido")
else:
    print(f'Você digitou: {numero3}')        

print(10*'-')

#tratando diversos erros
error = []#a lista onde vou guaradar os erros
try: #tentanto exercutar
    numerador2 = 10
    denominador2 = '0'
    resultado = numerador2 / denominador2
    print(resultado)
except ZeroDivisionError as e: #pegando a o erro e guarda em uma variavel
    print("Erro Divisão Por Zero")
    error.append(e)
    print(error)
except TypeError as e:
    print("Erro por Tipo De Dados")
    error.append(e)
    print(error)
print(10*'-')    