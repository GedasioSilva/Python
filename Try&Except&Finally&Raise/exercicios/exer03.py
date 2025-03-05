#faça um programa que recebe nome string , idade int , e peso float 
# se algum desses dados forem do tipo errado mostra um except do erro 

erros = [] #criando a lista que vai receber os dados

try:
    numero = int("abc")
    print(numero)
except ValueError as erro:
    erros.append(erro)
    print(f"Pega o nome do erro: " , erro.__class__.__name__)
    print(f"quantidade de Erros: {len(erros)}")


#pegando outro erro
print(10*'-')

try:
    a = 18
    b = 'c'
    soma = a + b
except TypeError as e:
    print(f'Pegando o nome do erro',e.__class__.__name__)



    
