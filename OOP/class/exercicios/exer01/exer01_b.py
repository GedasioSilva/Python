import json #importando o json

#ta falando que vou pegar do outro modulo 
# o caminho do json e os dados da class pessoa
from exer01_a import caminho_arquivo , Pessoa ,fazer_dump #ta chamando a função do dump

fazer_dump() #chamando a função

with open(caminho_arquivo,'r')as arquivo: #o r é pra ler os arquivos
    pessoas = json.load(arquivo) #pessoa vai receber os dados json salvo no arquivo
    #to pegando os dados da class e passando pros objetos
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1]) 
    p3 = Pessoa(**pessoas[2])  

    print(p1.nome,p1.idade)
    print(p2.nome,p2.idade)
    print(p3.nome,p3.idade)