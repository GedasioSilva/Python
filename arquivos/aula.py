#caminho completo pra abrir esse arquivo coloca 2 \\ onde tiver 1 e fechar com 2
caminho_arquivo = 'C:\\PYTHON\\Python\\arquivos\\'
caminho_arquivo += 'aula.txt' #comando pra adicionar uma arquivo que não existe
#verificar se o caminho estar correto
#print(caminho_arquivo)

#o open arir um arquivo só que o arquivo n existe ai coloco o 'w' se não tiver ele cria
#arquivo = open(caminho_arquivo,'w')
#arquivo.close() fechar o arquivo

#comando pra criar e fechar o arquivo
#depois que eu sair do with open o arquivo vai ser fechado
with open(caminho_arquivo,'w') as arquivo:
    #escrevendo coisas no arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n')
    print('Arquivo vai ser fechado')

