try:
    import aula_packge #aqui estou importando a Pasta
    from aula_packge.modulo import * #importando modulo
    print("Os Módulos foram importadaso")
except ValueError:
    print("Teve erro ao importa os módulos")

print(10*"--",'SEPARANDO')

#aqui o pacote age como se fosse um Módulo
print(aula_packge.dobra(2))

print(bemvindo())