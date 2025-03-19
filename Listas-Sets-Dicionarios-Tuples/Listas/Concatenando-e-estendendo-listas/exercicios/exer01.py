#diferentes de formas de concatenar Listas

#forma comum
lista1 = [1,2,3]
lista2 = [4,5,6]

listaSomada = lista1 + lista2
print(listaSomada)

print(30*'-')

#Utilizando o metodo Extend

lista3 = [1,2,3]
lista4 = [4,5,6]

lista3.extend(lista4)
print(lista3)


print(30*'-')

#Usando unpacking (*)

lista5 = [1, 2, 3]
lista6 = [4, 5, 6]
resultado = [*lista1, *lista2]
print(resultado)  
