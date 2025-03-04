# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)

lista = [] #considerado false
dicionario = {} #considerado false
conjunto = set() #considerado false
tupla = () #considerado false
string = '' #considerado false
inteito = 0 #considerado false
flutuante = 0.0 #considerado false
nada = None #considerado false
falso = False #considerado false
intervalo = range(0) #considerado false


def falsy(valor): #uma função que recebe um valor
    return 'falsy'if not valor else 'truthy'
    #retorno falsy if o valor for diferente de truthy

print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteito=}', falsy(inteito))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))