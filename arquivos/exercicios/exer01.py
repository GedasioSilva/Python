#pra pegar o caminho completo só abrir com o terminal
caminho = 'C:\\PYTHON\\Python\\arquivos\\exercicios\\'
caminho += 'exer01.txt' #se não exertir criar esse caminho

with open(caminho ,'w+',encoding='utf8') as arquivo:
    arquivo.write('Criando o conteudo do arquivo \n')
    arquivo.writelines(#escrevendo diversas linhas
        ('nome Gedasio \n','sobrenome silva \n')
    )
    arquivo.seek(0,0)
    print(arquivo.read())