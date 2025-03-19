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
b_1 = Button(frame_corpo, text="C",width=11, height=2,bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_1.place(x=0,y=0) #posições do eixo 
b_2 = Button(frame_corpo, text="%",width=6, height=2 , bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_2.place(x=118,y=0) #posições do eixo 
b_3 = Button(frame_corpo, text="/",width=6, height=2,bg=cor5,fg=cor2 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_3.place(x=177,y=0) #posições do eixo 



b_4 = Button(frame_corpo, text="%",width=6, height=2 , bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_4.place(x=0,y=0) #posições do eixo 
b_5 = Button(frame_corpo, text="/",width=6, height=2,bg=cor5,fg=cor2 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_5.place(x=0,y=0) #posições do eixo 
b_6 = Button(frame_corpo, text="/",width=6, height=2,bg=cor5,fg=cor2 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_6.place(x=0,y=0) #posições do eixo
b_6 = Button(frame_corpo, text="/",width=6, height=2,bg=cor5,fg=cor2 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_6.place(x=0,y=0) #posições do eixo  

janela.mainloop()