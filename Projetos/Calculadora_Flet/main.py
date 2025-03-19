from tkinter import * #importando o módulo
from tkinter import ttk

#variavel recebe os valores da cor preta
#sistemas de cores hexadecimais cores
cor1 = "#1e1f1e" #preta
cor2 = "#feffff" #branca
cor3 = '#38576b' #azul
cor4 = '#ECEFF1' #cinza
cor5 = '#FFAB40' #laranja


janela = Tk()
janela.title("Calculadora") #nome do projeto
janela.geometry("235x318") #dimensões
janela.config(bg=cor1)

#sistema de frames dominio de tela
frame_tela = Frame(janela,width=235,height=50 , bg=cor3) #dimensões
frame_tela.grid(row=0,column=0) #espaçamento


#tamanho da tela
frame_corpo = Frame(janela,width=235,height=268)
frame_corpo.grid(row=1,column=0)

#Criando botões
b_1 = Button(frame_corpo, text="C",width=11, height=2)
b_1.place(x=0,y=0) #posições do eixo 

janela.mainloop()