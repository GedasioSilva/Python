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

resultado = (num1 + num2) / 2

print("Sua nota foi " + "{:.1f}".format(resultado))

#end \r\n é utilizado pra quebrar a linha
print(12,34,sep=" - ",end='\r\n') #sep é o escapaço
print(10,40,sep=" ")
print("ola")

#dessa o valor maior_de_idade recebe um valor boleano tru ou false
maior_de_idade = idade >= 18
print(f'idade {idade} é maior de idade \n{maior_de_idade}')

#identidade de um objeto é quando uma variavel tem um código
#tipo cada conteudo de uma variavel tem um código pra ser chamado
#quando a pessoa chamar a variavel
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))