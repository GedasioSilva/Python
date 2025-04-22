def meu_decorador(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

@meu_decorador
def diga_ola():
    print("Olá")

diga_ola()

print("SEPARANDO O CONTEUDO")

def decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__} com args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorador
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print("Resultado:", resultado)


print("SEPARANDO O CONTEUDO")
        