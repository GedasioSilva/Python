nome = "João"
idade = 30

# Usando f-strings
print(f"Meu nome é {nome} e tenho {idade} anos.")

# Usando format()
print("Meu nome é {} e tenho {} anos.".format(nome, idade))

# Usando placeholders
print("Meu nome é %s e tenho %d anos." % (nome, idade))



texto = "Python é muito poderoso"
print(texto.startswith("Python"))  # True
print(texto.endswith("poderoso"))  # True
print(texto.find("muito"))         # 9
print(texto.count("o"))            # 4
