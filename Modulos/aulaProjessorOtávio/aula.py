# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

print('Este Módulo se chama',__name__) #quando o modulo é criado primeiro se chama main
try:#verifica se o módulo foi entrado
    import pessoa
    from pessoa import media
    print("O Módulo foi encontrado") 
except ModuleNotFoundError:  #se não for encontrado mostra essa mensagem  
    print("Modulos não encontrados")

print(media(8,9))

print(10*'-','SEPARANDO O CÓDIGO',10*'-')
print(" ")

#tentar importar um módulo invalido pra dar Erro
try:
    import pessoa
    from pessoa import mediaa
except:
    print("Modulos não encontrados")

#importando uma função com argumentos args
print(10*'-','SEPARANDO O CÓDIGO',10*'-')
print(" ")
try:
    import pessoa
    from pessoa import mostrar
    mostrar('Gedasio','Camila','Diana')
except NameError:
    print("Error no nome da função")
finally:
    print("CÓDIGO EXECUTADO")