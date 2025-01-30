#um sistema que inserir lista e apagar itens dentro de uma lista
#onde o usuario informa oque deseja realisar
import os

listaCompras =[]
while True:
    print("Selecione uma Opção")
    operacao = input("[i]inserir [a]pagar [l]istar: ").lower()

    if operacao == 'i':
        os.system('clear')
        inserir = input("Inserir: ")
        listaCompras.append(inserir)

    elif operacao == 'a':
        if len(listaCompras) == 0:
            print("Não foi possivel apagar pos não tem items")
        else:    
            apagar = input("Apagar: ")
            listaCompras.remove(apagar)

    elif operacao == 'l':
        if len(listaCompras) == 0:
            print("Não tem itens na lista: ")
        else:
            for compras in listaCompras:
                print(compras)
    else:
        print("Valor informado invalido:")
        break                