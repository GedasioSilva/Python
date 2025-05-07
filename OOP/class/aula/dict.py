#é um dicionario que salva os valores passados dentro de um  objeto
#ele tambem é os atributos dentro do objeto e da um retorno com os valores

class Pessoa:
    ano_atual = 2025 #atributo definido dentro da class

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #a variavel ano atual menos o self idade

#desempacotando um dicionario dentro de uma class
dados = {'nome': 'joao', 'idade': 35}
p1 = Pessoa(**dados)
#vars ele mostra os dados dentro da class parecido com dict porém o dict faz outras coisas
print(vars(p1))
'''
p1 = Pessoa('joao',35)
p2 = Pessoa('helena',12)
print(p1.__dict__) #vai retornar os valores dentro do objeto
p1.__dict__['outra'] = 'coisa' #vai criar outro atributo com o valor outra
print(p1.__dict__) #consultando o objeto com o atributo criado dentro do dict
del p1.__dict__['outra'] #apagar a chave outra que eu criei com o dict
print(p1.__dict__) #chama os dados
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento()) #chamando a funçao dentro da class com o valor do atributo padrão
print(p2.get_ano_nascimento())
'''