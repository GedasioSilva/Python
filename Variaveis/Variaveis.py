#Criando variaveis
nome = "Dasio"
print(nome)

#concatenação entre variaveis
dado , idade = 'Dasio', 28
print(dado,idade)

nome = str("gedasio silva").capitalize()
idade = int(29)

print(f'Seu nome é {nome} e sua idade é {idade}')

num1 = int(input("Informe a primeira nota: "))
num2 = float(input("informe a segunda nota: "))

resultado = num1 + num2 / 2

print("Sua nota foi " + "{:.1f}".format(resultado))