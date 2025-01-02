#Os operadores lógicos em Python são usados para combinar ou inverter expressões booleanas. Eles retornam um valor True ou False com base nas condições avaliadas.

#Operador And

x = 10
print(x > 5 and x < 15) #true
print(x > 5 and x > 20) #false

print("---------------------------------")

idade = 25
altura = 1.75
resultado = (idade >= 18) and (altura >= 1.70)
#str é pra transformar a variavel resultado em string
msg = "pode participar do evento? "  + str(resultado)
print(msg)

print("---------------------------------")
#operador Or
print(x > 5 or x > 20) #true pq a primeira condição e verdade
print(x < 5 or x > 20) #false pq ambas condições são falsas

porta = 'f'
janela = 'a'

#se uma condição for atendida o alarme vai ser disparado

alarme = (porta == 'a') or (janela == 'a')
msg = 'Alarme Disparado? ' + str(alarme)
print(msg)

print("---------------------------------")
#operador not Negação Lógica
x = True
y = False
print(not x) #false a inverte o true
print(not y) #true a inverte o false

print("---------------------------------")
#uso combinado de condicionais

idade = int(input("Digite sua Idade:"))
possui_cnh = input("Você tem CNH?  (s/n):")

if idade >= 18 and possui_cnh.lower() == 's':
    print("vocÊ pode Dirigir!")
else:
    print("você não pode Dirigir.")    
    
# Precedência dos Operadores Lógicos
# A ordem de avaliação segue a precedência:

# not (mais alto)
# and
# or (mais baixo
