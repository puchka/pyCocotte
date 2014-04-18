# -*- coding:Latin-1 -*-

from Tkinter import *

fen=Tk()
fen.title('Prototype : Cocotte 2')
can=Canvas(fen,width=400,height=400,bg='white')
can.grid()

# Variables

x, y = 200, 375

pan = PhotoImage(file ='panier.gif')
item = can.create_image(x, y, image =pan)

Button(fen,text='Quit',command=fen.quit).grid(row=1,
                                              column=1)

fen.mainloop()
fen.destroy()
