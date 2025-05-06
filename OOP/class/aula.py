# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:#cada classes cria um molde
    #def init é cra cria uma iniciação o self refere ao uso da class quando charmar o "p = pessoa"
    def __init__(self, nome, sobrenome):
        self.nome = nome #dessa forma estou passando os atributos pra dentro da class em nome
        self.sobrenome = sobrenome #a class recebe no atributo o valor passado na instancia P

p = Pessoa('gedasio','silva') #passando os valores pra dentro da class molde
print(p.nome)

print(15*"###")
print()

#criar uma classe com metodos
class Carro:
    #o self seguinifica que vamos colocar os atributos na propria class
    def __init__(self,nome):
        self.nome = nome #colocando o valor dentro do atributo nome   

    def acelera(self):#pra poder pegar os dados da instancia
        print(f'{self.nome} esta acelerando....') #representa que é na propria class

fusca = Carro('Fusca') #aqui ta mostando que estamos utilizando o molde da class
print(fusca.nome)
fusca.acelera() #esta chamando sem o print pq já tem print dentro da função

print(20*'-') #separando as duas chamadas de classes
celta = Carro('Celta') #aqui ta mostando que estamos utilizando o molde da class
print(celta.nome)
celta.acelera() #vai aparecer celta pos dentro da class foi passado nessa instancia o nome celta

