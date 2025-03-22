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
janela.geometry("235x310") #dimensões
janela.config(bg=cor1)

#sistema de frames dominio de tela
frame_tela = Frame(janela,width=235,height=50 , bg=cor3) #dimensões
frame_tela.grid(row=0,column=0) #espaçamento


#tamanho da tela
frame_corpo = Frame(janela,width=235,height=268)
frame_corpo.grid(row=1,column=0)

#variavel todos valores
todos_valores = ''

#string var recebe o valor em string
valor_texto = StringVar()

#criando função
def entrar_valores(event):
    global todos_valores #variavel vai receber os valores

    todos_valores = todos_valores + str(event)    
 
    #passando valor para A tela
    valor_texto.set(todos_valores)

#função pra calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(f' {str(resultado)}')

#função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")    


#criando o display da calculadora
#frame dela pq o label vai ta dentro da area cinza
#width e height pra ocupar o tamanho da tela ,padax o padding,enchor pra o resultado ficar na direita
#justify o bloco ficar na direita , os outros são cores , bg fundo ,fg letra
#textvariable é pra o valor da variavel testo ser passado
app_label = Label(frame_tela,textvariable=valor_texto,width=16,height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT,font=('Ivy 18'),bg=cor3,fg=cor2)
app_label.place(x=0,y=0)

#Criando botões
#primeira linha de boões
b_1 = Button(frame_corpo,command=limpar_tela ,text="C",width=11, height=2,bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_1.place(x=0,y=0) #posições do eixo 
b_2 = Button(frame_corpo,command=lambda: entrar_valores('%'),text="%",width=5, height=2 ,bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_2.place(x=118,y=0) #posições do eixo 
b_3 = Button(frame_corpo,command=lambda: entrar_valores('/'), text="/",width=5, height=2,bg=cor5,fg=cor2 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_3.place(x=177,y=0) #posições do eixo 

#Segunda linha de botões
b_4 = Button(frame_corpo,command=lambda: entrar_valores('7'), text="7",width=5, height=2,bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_4.place(x=0,y=52) #posições do eixo 
b_5 = Button(frame_corpo,command=lambda: entrar_valores('8'), text="8",width=5, height=2 , bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_5.place(x=59,y=52) #posições do eixo
b_6 = Button(frame_corpo,command=lambda: entrar_valores('9'), text="9",width=5, height=2 , bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_6.place(x=118,y=52) #posições do eixo  
b_7 = Button(frame_corpo,command=lambda: entrar_valores('*'), text="*",width=5, height=2,bg=cor5,fg=cor2 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_7.place(x=177,y=52) #posições do eixo 


#Terceira linha de botões
b_8 = Button(frame_corpo,command=lambda: entrar_valores('4'), text="4",width=5, height=2,bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_8.place(x=0,y=104) #posições do eixo 
b_9 = Button(frame_corpo,command=lambda: entrar_valores('5'), text="5",width=5, height=2 , bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_9.place(x=59,y=104) #posições do eixo
b_10 = Button(frame_corpo,command=lambda: entrar_valores('6'), text="6",width=5, height=2 , bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_10.place(x=118,y=104) #posições do eixo  
b_11 = Button(frame_corpo,command=lambda: entrar_valores('-'), text="-",width=5, height=2,bg=cor5,fg=cor2 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_11.place(x=177,y=104) #posições do eixo 


#quarta linha de botões
b_12 = Button(frame_corpo,command=lambda: entrar_valores('1'), text="1",width=5, height=2,bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_12.place(x=0,y=156) #posições do eixo 
b_13 = Button(frame_corpo,command=lambda: entrar_valores('2'), text="2",width=5, height=2 , bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_13.place(x=59,y=156) #posições do eixo
b_14 = Button(frame_corpo,command=lambda: entrar_valores('3'), text="3",width=5, height=2 , bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_14.place(x=118,y=156) #posições do eixo  
b_15 = Button(frame_corpo,command=lambda: entrar_valores('+'), text="+",width=5, height=2,bg=cor5,fg=cor2 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_15.place(x=177,y=156) #posições do eixo 

b_16 = Button(frame_corpo,command=lambda: entrar_valores('0'), text="0",width=11, height=2,bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_16.place(x=0,y=208) #posições do eixo 
b_17 = Button(frame_corpo,command=lambda: entrar_valores('.'), text=".",width=5, height=2 ,bg=cor4 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_17.place(x=118,y=208) #posições do eixo 
b_18 = Button(frame_corpo,command=calcular, text="=",width=5, height=2,bg=cor5,fg=cor2 , font=('Ivy 13 bold'),relief=RAISED , overrelief=RIDGE)
b_18.place(x=177,y=208) #posições do eixo


janela.mainloop()