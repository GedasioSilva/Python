#contro "k c" comenta tudo contro "k u " descomenta
#isinstance is a built-in Python function used to check if an object is an instance of a specified class or a tuple of classes. It returns True if the object matches the specified class (or classes) and False otherwise

#verifica se a variavel é do tipo especifico passado no print
x = 10
# b = 'sol'
# print(isinstance(x,int)) #verifica se é int
# print(isinstance(x,float)) #verifica se é float
# print(isinstance(x,str)) #verifica se é complexo
# print(isinstance(b,str)) #verifica se é complexo
# print(isinstance(b,complex))#verifica se é complexo

# print(isinstance (x, (int,float))) #verifica se é int ou float


x = 40 # o x recebe um novo valor
c = 3
r = x * c
print(r)

print(" ")
#outro exemplo de lista usando isintance
# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set): #verificando se é um set
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str): #verifica se é um str
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)): #verifica se é int ou float
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO') #outro retorno não sendo nenhum dos outros
        print(item)