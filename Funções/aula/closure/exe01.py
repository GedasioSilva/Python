'''
Uma função closure em Python ocorre quando uma função é definida dentro de outrae a função 
interna lembra o escopo das variáveis da função externa, mesmo após o término da execução desta.
Aqui está um exemplo simples de como criar e usar uma função closure:
'''

def saudacao(nome):
    # Função externa que define o nome
    def mensagem():
          # Função interna que usa a variável da função externa
        return f'Olá, {nome}'
    return mensagem
#Criando uma função closure com o nome "Maria"
diga_ola = saudacao("Maria")
# Chamando a função closure
print(diga_ola())

print(" ")

def contador(inicial):
    # Função externa define uma variável
    contador_atual = inicial

    # Função interna que "lembra" o estado de contador_atual
    def incrementar():
        nonlocal contador_atual  # Permite modificar a variável do escopo externo
        contador_atual += 1
        return contador_atual

    return incrementar  # Retorna a função interna

# Criando uma instância do contador que começa em 10
meu_contador = contador(10)

# Usando a closure
print(meu_contador())  # Saída: 11
print(meu_contador())  # Saída: 12
print(meu_contador())  # Saída: 13

# Criando outro contador separado
outro_contador = contador(20)
print(outro_contador())  # Saída: 21
print(outro_contador())  # Saída: 22
