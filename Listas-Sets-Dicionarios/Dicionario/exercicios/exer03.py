#utilizar as listas quando necessario pria um atributo e uma descrição

capitais = {
    'Brasil':'Brasilia',
    'Argentina':'Buenos Aires',
    'cuba':'Santiago',
    'Australia':'canberra',
    'canada':'Ottawa'
}

pais_usuario = input("Digite o Nome do Pais: ")

if pais_usuario in capitais:
    print(f"A Capital {pais_usuario} é {capitais[pais_usuario]}")
else:
    print("Desulpe não temos informações sobre a capital Desse Pais")



usuarios = {
    "admin": "1234",
    "joao": "senha123",
    "maria": "segredo"
}

login = input("Usuário: ")
senha = input("Senha: ")

if usuarios.get(login) == senha:
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")



usuario = {
    "nome": "Ana",
    "idade": 28,
    "email": "ana@email.com",
    "ativo": True
}

print(f'{usuario['nome']} Email:{usuario['email']}')