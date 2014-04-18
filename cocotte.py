# -*- coding:Latin-1 -*-

from Tkinter import *
from random import randrange

# Définition de fonctions

def kit():
    fen.quit()
    fen.destroy()

def depl(dx,dy):
    global x, y
    x, y = x+dx, y+dy
    can.coords(pot,x-15,y-15,x+15,y+15)

def cond1():
    global x,y,a,b,s,sco,ds
    if x-15<=a<=x+15 and y-15<=b<=y+15:
        s+= ds
        sco.set(str(s))
        a,b= 80,420
        can.coords(o1,a-5,b-5,a+5,b+5)

def depl1():
    global a, b, v
    b=b+v
    can.coords(o1,a-5,b-5,a+5,b+5)
    cond1()
    if b<415:
        fen.after(20,depl1)
    else:
        a,b= 80,20
        can.coords(o1,a-5,b-5,a+5,b+5)
        fen.event_generate('<Return>')

def cond2():
    global x,y, c,d, s,sco,ds
    if x-15<=c<=x+15 and y-15<=d<=y+15:
        s+= ds
        sco.set(str(s))
        c,d= 160,420
        can.coords(o2,c-5,d-5,c+5,d+5)

def depl2():
    global c, d, v
    d=d+v
    can.coords(o2,c-5,d-5,c+5,d+5)
    cond2()
    if d<415:
        fen.after(20,depl2)
    else:
        c,d= 160,20
        can.coords(o2,c-5,d-5,c+5,d+5)
        fen.event_generate('<Return>')

def cond3():
    global x,y, e,f, s,sco,ds
    if x-15<=e<=x+15 and y-15<=f<=y+15:
        s+= ds
        sco.set(str(s))
        e,f= 240,420
        can.coords(o3,e-5,f-5,e+5,f+5)

def depl3():
    global e,f,v
    f+=v
    can.coords(o3,e-5,f-5,e+5,f+5)
    cond3()
    if f<415:
        fen.after(20,depl3)
    else:
        e,f= 240,20
        can.coords(o3,e-5,f-5,e+5,f+5)
        fen.event_generate('<Return>')

def cond4():
    global x,y,g,h,s,sco,ds
    if x-15<=g<=x+15 and y-15<=h<=y+15:
        s+= ds
        sco.set(str(s))
        g,h= 320,420
        can.coords(o3,g-5,h-5,g+5,h+5)

def depl4():
    global g,h,v
    h+=v
    can.coords(o3,g-5,h-5,g+5,h+5)
    cond4()
    if h<415:
        fen.after(20,depl4)
    else:
        g,h= 320,20
        can.coords(o3,g-5,h-5,g+5,h+5)
        fen.event_generate('<Return>')

def gauche(event):
    global x
    if x<=15:
        pass
    else:
        depl(-7,0)

def droite(event):
    global x
    if x>=385:
        pass
    else:
        depl(7,0)

def moov(event):
    global ds, k, s
    k+= 1
    if k==40:
        # Fin du jeu
        f=open('hs','r')
        sc=f.readline()
        if int(sc)<s:
            can.create_text(200,100,text="Congratulations! You've \
get the high score.",font=('Times',12,'bold'),fill='blue')
            can.create_text(200,150,text="Score : "+str(s),
                            font=('Times',16,'bold'),fill='orange')
            f.close()
            f=open('hs','w')
            f.write(str(s))
        else:
            can.create_text(200,150,text="Score : "+str(s),
                            fon=('Times',20,'bold'),fill='blue')
        can.create_text(200,250,text='The End',
                        font=('Times', 20, 'bold'), fill ='red')
        f.close()
    else:
        n=randrange(4)
        n2=randrange(3)
        if n2==0:
            coul='orange'
            ds= 5
        if n2==1:
            coul='gray'
            ds= 20
        if n2==2:
            coul='brown'
            ds= -10
        if n==0:
            depl1()
            can.itemconfigure(o1,fill=coul)
        if n==1:
            depl2()
            can.itemconfigure(o2,fill=coul)
        if n==2:
            depl3()
            can.itemconfigure(o3,fill=coul)
        if n==3:
            depl4()
            can.itemconfigure(o4,fill=coul)
        msg.configure(text='')

# Programme principal

# Fenêtre principale
fen=Tk()
fen.title("Cocotte")
# Message d'accueil
msg=Label(fen,text='Appuyez sur Entrer pour commencer')
msg.grid(row=0,column=0,columnspan=2)
# Score
Label(fen,text='Score : ').grid(row=1,column=0)
sco=StringVar()
sco.set('0')
scr=Entry(fen,textvariable=sco)
scr.grid(row=1,column=1)
# Canevas
can=Canvas(fen,width=400,height=400,bg='white')
can.grid(row=2,column=0,columnspan=2)
# Bouton 'Quitter'
Button(fen,text='Quitter',command=kit).grid(row=3,
                                            column=2)

# Variables globales

x,y = 200, 385
a,b = 80,20
c,d = 160,20
e,f = 240,20
g,h = 320,20
v= 5
s=0
k=1

# Pot

pot=can.create_rectangle(x-15,y-15,x+15,y+15,fill='orange')

# Oeufs

o1=can.create_oval(a-5,b-5,a+5,b+5,fill='white')
o2=can.create_oval(c-5,d-5,c+5,d+5,fill='white')
o3=can.create_oval(e-5,f-5,e+5,f+5,fill='white')
o4=can.create_oval(g-5,h-5,g+5,h+5,fill='white')
# Paniers
can.create_rectangle(a-10,b-10,a+10,b+10,fill='yellow')
can.create_rectangle(c-10,d-10,c+10,d+10,fill='yellow')
can.create_rectangle(e-10,f-10,e+10,f+10,fill='yellow')
can.create_rectangle(g-10,h-10,g+10,h+10,fill='yellow')

fen.bind('<Left>',gauche)
fen.bind('<Right>',droite)
fen.bind('<Return>',moov)

fen.mainloop()
