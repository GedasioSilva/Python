# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2025 #atributo de class

    def __init__(self,nome,empresa):
        self.nome = nome
        self.empresa = empresa

    #utilizamos essa class quando temos um valor padrão tipo uma idade ai não precisa ficar passando o mesmo valor
    #exemplo uma empresa ai quem é da mesma impresa só criar essa class ai os dados são salvos
    @classmethod #posso chamar a minha class sem passar o self
    def empresa_farmacia(cls,nome): #porém sempre tem que receber um parametro cls = é um valor padrão
        return cls(nome,'farmacia diariamente') #quando eu chamar esse metodo eu preciso informa só o nome pq a impresa é padrão


p1 = Pessoa('joao','fiat')#pessoa que não tem a empresa padrão
print(vars(p1))
print()

p2 = Pessoa.empresa_farmacia('Gedasio') #informo só um dado pq a empresa é valor padrão
print(vars(p2))
print()
#print(p2.nome,p2.idade,p2.empresa)#chamando cada item
