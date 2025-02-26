#exemplo de uso dos sets

letras = set()
while True:
    letra = input("Digite: ").lower()
    letras.add(letra) #adicionar a letra digitada no set letras

    if 'l' in letras: #procurando a letra l entre as letras passada pelo usuario
        print('Parabéns você achou a letra encontrada')
        break
    print(letras)