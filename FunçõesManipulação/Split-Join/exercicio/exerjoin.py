#criar um join pra pegar um lista de nomer e colocar uma string pra separar

nomes = ['GEDASIO','DIANA','CAMILA','NUBIA']
print(*nomes)

#agora vou criar uma lista onde vou separar os items por barra

nomesBarra = ' | '.join(nomes)
print(nomesBarra)

print("-------------Separar-----------")

#o join é bem simples colocar strings pra separar os conteudos

palavras = ["Python", "é", "incrível"]
resultado = f" Alunos: {' | '.join(palavras)}"
print(resultado)  
