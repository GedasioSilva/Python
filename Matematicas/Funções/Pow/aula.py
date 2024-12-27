#potencialização
#primeiro número é o multiplicado e depois o multiplicador
print(pow(2,3))

valor = float(input("Qual o número vc que potencializar: "))
print(valor)

multiplicador = int(input("Informe o multiplicador: "))

potencia =(pow(valor,multiplicador))
print(" o valor da pontencia é " "{:.2f}".format(potencia))

if potencia % 2 == 0:
    print("valor é pá")
else:
    print("valor é Impar")    
    