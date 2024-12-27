#round é utilizado pra arredondar os números pra baixo ou pra cima

def mediaAluno(nota1,nota2):
    primeira = float(nota1)
    segunda = float(nota2)
    media = (primeira + segunda) /2
    if media >= 7:
        print("Aluno Aprovado")
        print(round(media,2)) #arredonda o número com 2 casas decimais
    else:
        print("Aluno reprovado")
        print(round(media,2))    

mediaAluno(7.359,3.333)

print(" ")
print("Segunda")

salario =5003.337
salarioFormatado = "{:.2f}".format(salario)

print(salario)
print(salarioFormatado)

print(" ")
print("Terceira")

primeiranota = float(input("Primeira Nota: "))
print("{:.2f}".format(primeiranota))
segundanota = float(input("Segunda Nota: "))
print("{:.2f}".format(segundanota))

print(round(primeiranota + segundanota,2))

