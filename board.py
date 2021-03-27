# GUI of my app
from tkinter import *

class application:
    def __init__(self):
        self.okno = Tk()
        self.platno = Canvas(self.okno, width=605, height=605)
        self.platno.pack()
        self.vytvorpapir()
        self.x = 0
        self.y = 0
        self.narade = 0
        self.hrajeme()

    def vytvorpapir(self):
        self.hraciplocha = []
        for i in range(15):
            self.hraciplocha.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        for i in range(15):
            for j in range(15):
                self.platno.create_rectangle(j*40+5,i*40+5,j*40+45,i*40+45,fill="white")

    def klik(self,eventorigin):
        self.x = eventorigin.x
        self.y = eventorigin.y
        self.x = int((self.x - (self.x % 40)) / 40)
        self.y = int((self.y - (self.y % 40)) / 40)
        self.malujeme()

    def malujeme(self):
        if (self.hraciplocha[self.x][self.y]==0):
            self.kdohraje()
            self.hraciplocha[self.x][self.y] = 1

    def kdohraje(self):
        if (self.narade==0):
            self.narade = 1
            self.malujkrizek(self.x,self.y)
        else:
            self.narade = 0
            self.malujkolecko(self.x,self.y)

    def hrajeme(self):
        self.okno.bind("<Button 1>",self.klik)
        self.platno.after(50,self.hrajeme)

    def malujkrizek(self,x,y):
        x *= 40
        y *= 40
        self.platno.create_line(x+5,y+5,x+45,y+45)
        self.platno.create_line(x+45,y+5,x+5,y+45)

    def malujkolecko(self,x,y):
        x *= 40
        y *= 40
        self.platno.create_oval(x+5,y+5,x+45,y+45)

    """
    KDO VYHRAL???
    """   

# app = application()
# mainloop()    