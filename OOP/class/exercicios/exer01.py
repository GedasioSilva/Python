#criar uma classe de um carro com nome ano e descricao

class Carro:
    def __init__(self,nome,ano,descricao): #self se refere a class 
        self.nome = nome
        self.ano = ano
        self.descricao = descricao

    def verifica_ano(self): #funçao verifica se o ano do carro é menor de 2010
        if self.ano > 2010:
            return 'o ano do carro é valido'
        else:
            return 'ano do carro não é valido'

    def ipva_pago(self,comprovante): #verifica se o valor do ipva foi pago
        if comprovante == True:
            return 'valor do ipva foi pago'
        else:
            return 'valor do ipva não foi pago'
        
    def verifica_proprietario(self,cpf_dono): #verica se é o dono cadastrado
            codigo = 123
            if codigo == cpf_dono:
                return 'esta apito a conduzir'
            else:
                return 'não estar apito'


fiat = Carro('palio',2016,'completo')
print(vars(fiat)) #mostrando o conteudo da classe fiat
print(fiat.verifica_ano()) #chamando a funçao com o valor 
print(fiat.ipva_pago(False))
print(fiat.verifica_proprietario(234))

##criar outra class com o modulo de carro
print('SEPARANDO O CONTEUDO DOS CLASSES')
print()

ford = Carro('onix',2018,'vidro e ar')
print(vars(ford))
print(ford.verifica_ano()) #chamando a funçao com o valor 
print(ford.ipva_pago(True))
print(ford.verifica_proprietario(123))

