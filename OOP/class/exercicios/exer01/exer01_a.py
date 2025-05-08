#vou criar uma class e passar os dados dela pro json
#depois vou criar outro modulo e acessar os dados dela que estão salvos no json
import json
caminho_arquivo = 'C://PYTHON//Python//OOP//class//exercicios//exer01//' #caminho onde vai criar o arquivo
caminho_arquivo += 'aula127.json' #pra abrir o arquivo se não tiver cria

class Pessoa: #class
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)] #a lista bd tem que receber os dados pro vars

def fazer_dump(): #uma função onde vai fazer a chamada do arquivo
    with open(caminho_arquivo, 'w',encoding='utf8') as arquivo: #aqui pra abrir o aquivo , w pra ler e escrever
        print('Fazendo o dump') 
        json.dump(bd, arquivo, ensure_ascii=False, indent=2) #json utilizar o json

#verifica se é o main principal do arquivo
if __name__ == '__main__':
    print('Ele é o __main__')
    fazer_dump()