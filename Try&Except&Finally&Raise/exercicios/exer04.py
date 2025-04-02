#vou passar dados pra pra variaveis e dando o erro vou criando try except e finaly 

#informe seu nome 
erros =[] #lista onde vou guarda os erros
print(type(erros))

#tratando os erros no nome 
while True:
    try:
        idade = int(input("Informe sua idade: "))
        print(f'{idade} é um int')
        break
    except ValueError as erro:
        print("Idade informada foi invalida")
        erros.append(erro)



print(15*'-',"SEPARANDO O CONTEUDO")

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou: {numero}")
        break  # Se for válido, sai do loop
    except ValueError as erro:
        print("Entrada inválida! Tente novamente.")
        erros.append(erro)

print("Lista de erros")
for erroachado in erros:
    print(erroachado)

print(15*'-',"SEPARANDO O CONTEUDO")

#vou fazer uma uma função que recebe sua senhar

def senhar_valida(senhar):
    if senhar != 123: #se essa condição for atendida
        raise ValueError('Sua senhar é diferente')
    return "Senhar valida" #o retorno se o valor for valido

try: #tentando executar
    print(senhar_valida(123))
except ValueError: #deu erro
    print("ERRO ENCONTRADO")