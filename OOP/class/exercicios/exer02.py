#vou criar uma class de cantor e verificar se vai tar no show e usar dick

class veiculor:
    def __init__(self,modelo,ano):
        self.modelo = modelo
        self.ano = ano

    def verifica_ano(self):
        if self.ano == 2010:
            return 'valido'
        else:
            return 'invalido'
        
    def verifica_chassi(self):
        #o valor foi criado no dict lá em baixo porém quando chama a class enviar as alterações
        if self.chassi == True: 
            return 'valido'
        else:
            return 'invalido'


xtz = veiculor('xtz 125',2010)
print(vars(xtz))
print(xtz.verifica_ano())

dados_fan = {'modelo':'fan 160','ano':2018} #tem que colocar chave e valor
fan = veiculor(**dados_fan)
print(vars(fan))
fan.__dict__['chassi'] = True
print(vars(fan))
print(f'chassi é valido: {fan.verifica_chassi()}') #chamando o valor criado no dict