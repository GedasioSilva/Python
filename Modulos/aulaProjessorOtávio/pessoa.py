print("Conteudo do Módulo pessoa")
def media(n1,n2):
    media = n1 + n2 /2
    return f'{media:.2f}'

def mostrar(*args):
    for nome in args:
        print(nome)