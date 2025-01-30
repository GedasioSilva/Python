import os

palavra_secreta = 'diana'
letras_acertadas = ''
tentativas = 0

while True: #o sistema vai ficar rodando até parar o While
    #o usuario digita uma letra
    letra_digitada = input("Digite um Letra da Palavra Secreta: ")
    #toda as vezes que o input vai ser utilizado tentativas recebe 1
    tentativas += 1
    #verifica se o usuario digitou mais que uma letra
    while len(letra_digitada) > 1:# se for maior que 1 volta pro input
        print("Digite Apenas uma letra: ")
        continue

    #verifica se a letra digitada ta na palaravra
    # se tiver letra acertadas recebe a letra que ta na palavra    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    #aqui o letra cria um for com index letra_secreta pra rodar
    #se letra_secreta que são os index da palavra secreta tiver em letras acertada
    #print letra secreta
    #palavra formada pra receber a letra
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            #a palavra formada recebe a letra se tiver certo
            palavra_formada += letra_secreta
        else:
            #se tiver errada ela vai receber o asteristico
            palavra_formada += '*'
    print('Palavra Formada ', palavra_formada)        
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Você Ganhou Parabéns') 
        print(f'A Palavra secreta era {palavra_secreta}')
        print(f'Tentativas {tentativas}')
        letras_acertadas = ''
        tentativas = 0     