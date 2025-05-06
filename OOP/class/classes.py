#class são utilizadas pra guardar dados e representar Objetos
class Funcionarios:
    #pass  informa que a class é vazia
    nome ='Gedasio'
    sobreNome = 'silva'
    data_nascimento = '17/12/1995'

usuario1 = Funcionarios() #criando o objeto pegando dados de funcionario

print(usuario1.nome)
print(usuario1.data_nascimento)

print(10*'-','ESPOCO DE CLASSES')

#o escopo da classe só pode executar oque estiver dentro dela 
class Animal:
    def __init__(self,nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel) #vai exercutar quando estanciar a classe

    def comendo(self,alimento): # a classe tem um metodo comendo
        return f'{self.nome} está comendo... {alimento}'        
    

leao = Animal('Leão') # a class animal estar passando pra variavel noome
print(leao.nome) #chamando a varial nome
print(leao.comendo('maça')) # a classe animal ta passando pra função comendo o atributo alimento

print(10*'-','Estados dentro de uma classes')

class Camera:
    def __init__(self,nome,filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self): #quando chamar essa função o atributo filmando vai receber o true
        if self.filmando: #se o filmando for true sai isso
            print(f'{self.nome} já esta filmando') #aqui caso essa função for chamada 2 vezes seguidas
            return #chegando aqui o código para
        
        print(f'{self.nome} Está filmando...') #chamando a função esse é o retorno da função
        self.filmando = True #self pós ta pegando da propria classe

    def parar_filmar(self): 
        if not self.filmando: #aqui verifica se não esta filmando  
            print(f'{self.nome} não esta filmando') 
            return #chegando aqui o código para
        
        print(f'{self.nome} Está parando de  filmar...') #chamando a função esse é o retorno da função
        self.filmando = False #self pós ta pegando da propria classe

    def fotografar(self):    
        if self.filmando: #se o filmando for true sai isso
            print(f'{self.nome} não pode fotografar filmando') #aqui caso essa função for chamada 2 vezes seguidas
            return #chegando aqui o código para
        
        print(f'{self.nome} está fotografando....')
       

c1 = Camera('canon')        
c2 = Camera('sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()