#exercitar um pouco onde foi passando valores vazios 
#verificando se é false e truthy
#temos que saber se um valor é verdadeiro ou falso pra definir condições


lista = ('')
nome = '0'
sobrenome = None
valida = False
inteiro = 1

def verifica(valor):
    return 'falso' if not valor else 'Verdadeiro'

print(verifica(nome)) #uma string com dados é verdadeira
print(verifica(lista)) #uma string vazia é falso
print(verifica(sobrenome)) #None é considerado falso
print(verifica(valida)) #None é considerado falso
print(verifica(inteiro)) #None é considerado falso

