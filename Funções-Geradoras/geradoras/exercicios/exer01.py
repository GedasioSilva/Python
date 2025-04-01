#exemplo vai adicionando até 

def contador(maximo): #funcao recebe um valor
    contador_atual = 1 #contador atual começando com zero
    while contador_atual <= maximo: #enquanto o contador atual for menor que maximo
        yield contador_atual #contador pausando em cada ação do loop
        contador_atual += 1 #contador recebendo +1 ai no proximo loop mostra outro valor


for numero in contador(5):
    print(numero)

print("Outro exemplo de função Geradora") 

#a função verifica se o numero informado * 10 passa de 99
def multiplicador(n):
    multiplicador = 10
    resultado = multiplicador  * n
    print(resultado)
    if resultado >= 99:
        yield f'{resultado} valor maximo alcançado'

for index in multiplicador(10):
    print(index)