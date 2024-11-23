#tratamento de Erros caso o valor se invalidado é jogado em ValueError onde output o retorno

try:
    idade = int(input("Digite sua idade: "))
except ValueError:
    print("Porfavor, insira um número Válido: ")    