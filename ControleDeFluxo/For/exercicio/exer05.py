print(" ")
print("úsuario Bloqueado")

print("Opção 1 Verificação Pelo Email: ")
print("Opção 2 Verificação Pelo Celular: ")
escolhar = input("Digite a Opção Escolhida: ")

def recuperacao(escolhar):
    if int(escolhar) == 1:
            print("Email pra alterar senhar Enviado")     
    elif int(escolhar) == 2:
            print("SmS Enviado pro seu Número:")
    else:
          print("Opção Escolhida foi Invalida: ")
recuperacao(escolhar)