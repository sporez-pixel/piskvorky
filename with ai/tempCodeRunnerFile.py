self.x = eventorigin.x
        self.y = eventorigin.y
        self.x = int((self.x - (self.x % 40)) / 40) # převádí souřadnice na adresu políček
        self.y = int((self.y - (self.y % 40)) / 40)
        self.malujeme() # maluje, na místo, kde hráč kliknul
        self.vyhralnekdo()