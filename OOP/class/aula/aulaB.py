#criar a classe
class Funcionarios:
    pass

#criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

#criar os parametros do usuario1
usuario1.nome = 'Elena'
usuario1.sobreNome = 'cabral'
usuario1.data_nascimento = '12/01/2009'

#print usuario01
print(usuario1.nome)
print(usuario1.data_nascimento)

print(" ")

#criar os parametros do usuario2
usuario2.nome = 'Carol'
usuario2.sobreNome = 'silva'
usuario2.data_nascimento = '15/10/2005'

#print usuario02
print(usuario2.nome)
print(usuario2.sobreNome)

print(10*'#','SEPARANDO O CONTEUDO')
print()

#atributos na class sao atributo que são definidos dentro da classe

class Pessoa:
    ano_atual = 2025 #atributo definido dentro da class

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #a variavel ano atual menos o self idade
    

p1 = Pessoa('joao',35)
p2 = Pessoa('helena',12)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento()) #chamando a funçao dentro da class com o valor do atributo padrão
print(p2.get_ano_nascimento())

    


        