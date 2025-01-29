#contar qual é a letra que mais apareceu na frase
frase = 'o Python é uma linguagem de programação multiparadigma Python foi criado por Guido van Rossum.'

#conta quantas vezes o 'Python' na frase
print(frase.count('Python'))

i = 0
qtd_pareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_pareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_pareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print(f'A letra que mais repetiu foi "{letra_apareceu_mais_vezes}" vezes {qtd_pareceu_mais_vezes}')

print(" ")



