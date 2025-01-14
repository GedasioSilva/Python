#função pega um valor e tira a raiz quadrada do valor
def quadrado(numero):
    return numero ** 2

num = int(input("Digite um Número: "))
print(f'O quadrado de {quadrado(num)}')

#função pegas os items da lista e insere na função

numeros = [1,2,3,4,5,7,8,9,10]

def eh_par(numero):
    return numero % 2 == 0

pares = filter(eh_par,numeros)
print(list(pares))

#outro exemplo de pegar os items da lista e inserir na função

nomes = ["Ana", "João", "Maria", "Carlos", "Bia"]

def mais_de_tres_caracteres(nome):
    return len(nome) > 3

nomes_filtrados = filter(mais_de_tres_caracteres,nomes)
print(list(nomes_filtrados))

