#format é utilizado pra fazer a formatação das casas decimais 

dolarHoje = 6.3999
print(dolarHoje)

#dolar formadato com apenas duas casas decimais
print("{:.2f}".format(dolarHoje))

valor1 = 3.888
valor2 = 4.9998
soma = valor1 + valor2
#nota sendo formatada com apenas duas casas Decimais
print("{:.2f}".format(soma))

print(" ")


#mostra que vai receber a formatação é o dollar é passado
texto = "valor do Dollar hoje:{:.2f}"
dollar = 6.399
print(texto.format(dollar))


#usando diferentes placeholders values
#o format esta recebendo os valores 
texto01 = "Meu nome é {fname} , eu tenho {idade}".format(fname="john" , idade = 29)
print(texto01)