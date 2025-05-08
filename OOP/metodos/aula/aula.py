from datetime import datetime
#construtor inicia o objeto com parametros

#criar a classe
class Funcionarios:
   #sef pra passar pros objetos
    def __init__(self,nome,sobreNome,ano_nascimento):
        self.nome = nome
        self.sobreNome = sobreNome
        self.ano_nascimento = ano_nascimento 
        
    def nome_completo(self): 
            return self.nome + ' ' + self.sobreNome
          
            
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
    

#criar o objeto e passando os dados pro construtor da class
usuario1 = Funcionarios('Elena','cabral',2009)
usuario2 = Funcionarios('Carol','silva',2005)
usuario3 = Funcionarios('Andre','Iacono',2003)

#print imprimindo o objeto
print(usuario3.nome)

#chamando a função dentro da class
print(usuario1.nome_completo())
print(usuario2.nome_completo())
#outra forma de imprir a função
print(Funcionarios.nome_completo(usuario3))
print(Funcionarios.idade_funcionario(usuario3))

