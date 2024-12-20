#construtor inicia o objeto com parametros

#criar a classe
class Funcionarios:
   #sef pra passar pros objetos
   def __init__(self,nome,sobreNome,data_nascimento):
      self.nome = nome
      self.sobreNome = sobreNome
      self.data_nascimento = data_nascimento

#criar o objeto e passando os dados pro construtor da class
usuario1 = Funcionarios('Elena','cabral','12/01/2009')
usuario2 = Funcionarios('Carol','silva','15/10/2005')
usuario3 = Funcionarios('Andre','Iacono','11/03/2003')


#print imprimindo o objeto
print(usuario1.nome)
print(usuario2.nome)
print(usuario3.nome)