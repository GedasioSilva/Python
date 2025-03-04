
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operação finalizada.")

dividir(10, 2)

print(" ")

def media(a,b):
    try:
        resultado = a / b
    except:
        print('vamos ver')
    else:
        print(f"Resultado: {resultado}")        


media(9,0)