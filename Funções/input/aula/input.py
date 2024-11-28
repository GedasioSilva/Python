#Em Python, a função input() é usada para capturar dados fornecidos pelo usuário no terminal. Ela retorna os dados como uma string.

#Entrada Básica
# nome = input("Digite seu nome: ")
# print("olá",nome)

#Convertendo para Outros Tipos
# idade = int(input("Digite sua Idade:" ))
# print("Você tem " , idade , "Anos")

#Entrada de um número decimal (float):
#deve ser informado com ponto não virgula
# altura = float(input("Digite sua Altura em Metros:" ))
# print("Sua Altura é: " , altura)

#Entrada com Vários Valores
# dados = input("Digite seu nome e idade separados por espaço: ").split()
# nome = dados[0]
# idade = int(dados[1])
# print(f"Nome:{nome} , Idade {idade}")


#entrada de dados simples
# loguin = input("Digite seu loguin:")
# senha = input("Digite sua senhar: ")
# print(f" Seu loguin é : {loguin} sua Senhar é {senha}")

nome = str(input("Qual é o seu nome: " ))
idade = str(input('Qual é a sua idade: '))
cidade = input('Onde você mora: ')
print(nome)
print('seu Nome ' + nome + ' e  a sua Idade ' + idade + ' onde vc mora ' + cidade)