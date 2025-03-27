#Filtro de dados em list comprehension (filter)
#vai rodar um loop e cada vez o n vai receber 1
#tudo que for escrito antes do if são map e depois do if são filtros
lista = [n for n in range(10) if n < 5] #adiciona até o n for menor que 5
print(lista)

print(1* '\n')

#esta retornando se a palavra for maior que 5 letras
palavras = ["Python","Java","C","Javascript","Golang"]
longas = [palavra for palavra in palavras if len(palavra) > 5]
print(longas)

print(1* '\n')

#exemplo pra retornar apenas nomes que começem com a letra 
nomes2 = ["Alice", "Bruno", "Ana", "Carlos", "Amanda"]
nomes_com_a = [nome for nome in nomes2 if nome.startswith("A")]
print(nomes_com_a)
print(1*'\n')

#criar diversos numeros de 1 até 50
numeros3 = range(1,50)
#verifica ser o x é divisivio por 3 e o resto é 0
divisiveis = [x for x in numeros3 if x % 3 == 0 ]
print(divisiveis)

print(1*'\n')

#verificar se o número é pa ou não
#vou usar o numeros3
par = [x for x in numeros3 if x % 2 == 0]
print(par)