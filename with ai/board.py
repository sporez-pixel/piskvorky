# GUI of my app
from tkinter import *
from vyhra import *

class application:
    def __init__(self):
        self.okno = Tk()
        self.platno = Canvas(self.okno, width=609, height=609)
        self.platno.pack() # vytváří plátno o velikosti 609x609
        self.vytvorpapir() # zpouští funkci, která maluje hrací papír
        self.narade = 1 # proměná, která sleduje, která sleduje kdo je na tahu
        self.tahu = 0 # proměná, která sleduje kolik tahů se hrálo
        self.vyhral = False # boolean proměná, která sleduje, jestli někdo nevyhrál
        self.computer = computer()
        self.hrajeme() # veškerá logika hry se odehrává v této funkci

    def vytvorpapir(self): # vytváří 2D list, ve kterém se ukládají data
        self.hraciplocha = []
        for i in range(15):
            self.hraciplocha.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        for i in range(15):
            for j in range(15):
                self.platno.create_rectangle(j*40+5,i*40+5,j*40+45,i*40+45,fill="white")

    def klik(self,eventorigin): # funkce, která sleduje, na které políčko hráč kliknul
        self.x = eventorigin.x
        self.y = eventorigin.y
        self.x = int((self.x - (self.x % 40)) / 40) # převádí souřadnice na adresu políček
        self.y = int((self.y - (self.y % 40)) / 40)
        self.malujeme() # maluje, na místo, kde hráč kliknul
        self.vyhralnekdo() # funkce, která kontroluje, jestli někdo nevyhrál

    def malujeme(self):
        if (self.hraciplocha[self.y][self.x]==0): # maluj pokud na místo, kde hráč kliknul, pokud tam už někdo předtím nemaloval
            self.kdohraje() # v této funkci ještě kontroluji kdo hraje, tudíž co se maluje O nebo X
            self.vyhral = vyhra(self.hraciplocha, self.x, self.y, self.narade) # funkce, která se kouká, jestli někdo nevyhrál
        

    def kdohraje(self): # zde se jen program kouká kdo hraje, totiž co má malova a kam
        # když je na řade hráč 1 self.narade = 1
        # když je na řadě hráč 2 self.narade = 2
        if (self.narade==1):
            self.narade = 2
            self.malujkrizek(self.x,self.y)
            self.hraciplocha[self.y][self.x] = 1

        else:
            self.narade = 1
            self.malujkolecko(self.x,self.y)
            self.hraciplocha[self.y][self.x] = 2

    def hrajeme(self):
        # tady jen pozorujeme klik hráčů
        self.okno.bind("<Button 1>",self.klik)
        self.computerMove()
        self.platno.after(50,self.hrajeme) # po 50 milisekundách se zpouští hlavní funkce, kde probíhá celá hra

    def malujkrizek(self,x,y): # abych to měl jednoduší, tady mám definované, co má tkinter dělat, aby namaloval křížek
        x *= 40
        y *= 40
        self.platno.create_line(x+5,y+5,x+45,y+45)
        self.platno.create_line(x+45,y+5,x+5,y+45)
        self.tahu += 1

    def malujkolecko(self,x,y): # abych to měl jednoduší, tady mám definované, co má tkinter dělat, aby namaloval kolečko
        x *= 40
        y *= 40
        self.platno.create_oval(x+5,y+5,x+45,y+45)

    def vyhralnekdo(self): # tady ve funkci se pouze koukáme, jestli už někdo vyhrál a pokud ano, tak ať se hra vypne
        if (self.vyhral):
            if (self.narade==1):
                self.hrac = 2
            else:
                self.hrac = 1
            self.platno.create_text(304.5,203,text="GAME OVER",font=["Arial",50],fill="red")
            self.okno.after(1000, self.textc)
            self.okno.after(5000, self.okno.quit)

    def textc(self): # abych to měl jednoduší, tady mám definované, co má tkinter dělat, aby napsal text
        self.platno.create_text(304.5, 304.5, text="Player "+str(self.hrac)+" won", font=["Arial",30], fill="black")

    def computerMove(self): # a function that interacts with the class computer
        self.computer.getBoard(self.hraciplocha)
        # self.x, self.y = 
        self.kdohraje()
        pass
