#exercitando os metodos que são usados nos dicionarios
#criar um dicionario

dados = {
        'nome':'gedasio',
        'sexo':'masculino',
        'profissao':'Dev'
}
#definindo um valor padrão
dados.setdefault('idade',0)
#se o valor for zero pede pra adicionar um valor
if dados['idade'] == 0:
    print('Valor idade não informada , informe')
    dados['idade'] = input("Informe sua idade: ")
else:
    print("Idade adicionada")    

print(dados['idade']) #verifica se a idade foi adicionada

print(10*'-','Separando')

del dados['profissao'] #removendo o campo profissão
print(dados)
#print(type(dados)) verifica qual é o tipo se é dic list ou tuple

#agora vou atualizar todos os items da lista

dados.update({
    'nome':'Camila',
    'sexo':'feminino',
    'profissao':'professora'
})

print(dados)