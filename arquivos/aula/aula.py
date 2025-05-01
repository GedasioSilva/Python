import os
#caminho completo pra abrir esse arquivo coloca 2 \\ onde tiver 1 e fechar com 2
caminho_arquivo = 'C:\\PYTHON\\Python\\arquivos\\aula\\'
caminho_arquivo += 'aula.txt' #comando pra adicionar uma arquivo que não existe
#verificar se o caminho estar correto
#print(caminho_arquivo)

#o open arir um arquivo só que o arquivo n existe ai coloco o 'w' se não tiver ele cria
#arquivo = open(caminho_arquivo,'w')
#arquivo.close() fechar o arquivo

#comando pra criar e fechar o arquivo
#depois que eu sair do with open o arquivo vai ser fechado
"""
with open(caminho_arquivo,'w+',encoding='utf8') as arquivo: #o "+" pra habilitar a leitura 
    #escrevendo coisas no arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n')
    arquivo.writelines(#pra escrever diversas linhas
        ('linha 3 \n','linha 5 \n')
    )
    arquivo.seek(0,0) #seek é pra ler dentro do arquivo
    print(arquivo.read())
    print('lendo')
    arquivo.seek(0,0)
    print(arquivo.readline().strip()) #readline é pra ler a proxima linha
    print('READLINES')
    for linha in arquivo.readlines():
        print(linha.strip())

print('#' * 10)

with open(caminho_arquivo,'r') as arquivo:
    #escrevendo coisas no arquivo
    print(arquivo.read()) #read é ler o arquivo
"""
"""
#quando criamos com o a o arquivo anterio não é apagado
with open(caminho_arquivo,'a+') as arquivo:
        #escrevendo coisas no arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 1\n')
    arquivo.writelines(#pra escrever diversas linhas
        ('linha 3 \n','linha 5 \n')
    )
    print(arquivo.read())

"""

with open(caminho_arquivo,'w+',encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.writelines(
        ('linha 1 \n','linha 2 \n')
    )
    arquivo.seek(0,0)
    print(arquivo.read())
#os.remove(caminho_arquivo) #os.remove pra apagar o arquivo    
#os.rename(caminho_arquivo,'aula2.txt') rename renomeira ou move