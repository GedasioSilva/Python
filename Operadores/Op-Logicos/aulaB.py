#Operadores in e not in
#string sao iteráveis a string pode navegar entre index

nome = 'otavio'
print(nome[2]) #pegando "a" pelo número da index

print('a' in nome) #verifica se a letra a tem na String
print('z' in nome) #verifica se z tem em nome

if 'o' in nome:
    print("A letra esta na String")
else:
    print("A letra não está na String: ")    

print(10 * '-')

#verifica se a letra não esta na string se não tiver é true
print('g' not in nome)
print('v' not in nome)

if 'o' not in nome:
    print("A Não letra esta na String")
else:
    print("A letra  está na String: ")    

#encontrar a palavra Python na frase
palavra = "Python"  
frase =  "Python é uma boa linguagem de programação"

if palavra in frase:
    print(f'A palavra {palavra} Está na frase: "{frase}"')