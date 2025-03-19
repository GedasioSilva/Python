#criar um exercicio onde eu pego os 
#valores e crio uma tabela com index

nomesAlunos = [
    'GEDASIO','DIANA','NUBIA','CAMILA',
    'TINO','TIETA','BRANCO'
]

for index , nome in enumerate(nomesAlunos,start=1):
    print(f"Ó código: {index} nome {nome}")

print(" ")
print(15*"-",'SEPARANDO CONTEUDO',15*"-")

#VERIFICAR SE A CONTIDADE DE ALUNOS ESTA 
#CORRETA OU SE TEM MUITOS OU POUCOS

if len(nomesAlunos) < 7:
    print("Esta faltando algúem")
elif len(nomesAlunos) > 7:
    print("Tem muita gente")
else:
    print("A Contidade de Alunos esta correta: ")



