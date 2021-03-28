# GUI of my app
from tkinter import *
from vyhra import *

class application:
    def __init__(self):
        self.okno = Tk()
        self.platno = Canvas(self.okno, width=609, height=609)
        self.platno.pack()
        self.vytvorpapir()
        self.narade = 1
        self.tahu = 0
        self.vyhral = False
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
        print(self.x, self.y)
        self.printseznam()

    def malujeme(self):
        if (self.hraciplocha[self.y][self.x]==0):
            self.kdohraje()
        if (self.tahu >= 5):
            self.vyhral = vyhra(self.hraciplocha, self.x, self.y, self.narade)
        if (self.vyhral):
            print("VYHRA!")

    def kdohraje(self):
        if (self.narade==1):
            self.narade = 2
            self.malujkrizek(self.x,self.y)
            self.hraciplocha[self.y][self.x] = 1

        else:
            self.narade = 1
            self.malujkolecko(self.x,self.y)
            self.hraciplocha[self.y][self.x] = 2

    def hrajeme(self):
        self.okno.bind("<Button 1>",self.klik)
        self.platno.after(50,self.hrajeme)

    def malujkrizek(self,x,y):
        x *= 40
        y *= 40
        self.platno.create_line(x+5,y+5,x+45,y+45)
        self.platno.create_line(x+45,y+5,x+5,y+45)
        self.tahu += 1

    def malujkolecko(self,x,y):
        x *= 40
        y *= 40
        self.platno.create_oval(x+5,y+5,x+45,y+45)

    def printseznam(self):
        for s in self.hraciplocha:
            print(s)
