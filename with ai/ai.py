# algorithm - minimax
from vyhra import *
from random import randint

class computer:
    def __init__(self):
        self.whatToCheck = [[1,1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1],[1,-1],[-1,1]]
        self.moved = 0
        self.allMoves = []
    
    def minimax(self, depth, isMaximazing, lastMoves):
        someonewon = vyhra(self.board, lastMoves[0], lastMoves[1], self.switch(isMaximazing))
        if someonewon and isMaximazing:
            return 100

        if someonewon:
            return -100

        if depth<0:
            var = self.evaluation(lastMoves, isMaximazing)
            if var>-1: print(lastMoves, var)
            return var
        
        if (isMaximazing):
            bestScore = -10000000
            for l in self.whatToCheck:
                x = lastMoves[0]+l[0]
                y = lastMoves[1]+l[1]
                if self.possible(x,y):
                    self.board[y][x] = 2
                    score = self.minimax(depth-1, False, [x,y])
                    self.board[y][x] = 0
                    bestScore = max([score,bestScore])
            return bestScore

        else:
            bestScore = 10000000
            for l in self.whatToCheck:
                x = lastMoves[0]+l[0]
                y = lastMoves[1]+l[1]
                if self.possible(x,y):
                    self.board[y][x] = 1
                    score = self.minimax(depth-1, True, [x,y])
                    self.board[y][x] = 0
                    bestScore = min([score,bestScore])
            return bestScore

    def getBoard(self, board):
        self.board = board

    def computerMove(self,lastMoves):
        # possible = False
        # while(possible == False):
        #     x,y = self.randomMove()
        #     possible = self.possible(x,y)
        self.moved += 1
        bestScore = -10000000000
        self.allMoves.append(lastMoves)
        for l1 in self.allMoves:
            for l2 in self.whatToCheck:
                x = l1[0]+l2[0]
                y = l1[1]+l2[1]
                if self.possible(x,y):
                    self.board[y][x] = 2
                    score = self.minimax(2, True, [x,y])
                    self.board[y][x] = 0
                    if score>bestScore:
                        print('best score = '+str(score))
                        print(x,y)
                        bestScore = score
                        rx = x
                        ry = y
        self.allMoves.append([rx,ry])
        return rx,ry

    def searchMoves(self):
        pass

    def randomMove(self):
        x = randint(0,14)
        y = randint(0,14)
        return x,y

    def possible(self,x,y):
        if (x<15 and x>=0) and (y<15 and y>=0):
            if self.board[y][x] == 0:
                return True
            return False
        return False

    def switch(self, bool):
        if bool:
            return 2
        return 1

    def evaluation(self, lastMoves, isMaximazing): # so far I will just evaluate a position based on how many moves they need to win
        x,y = lastMoves[0], lastMoves[1]
        boardCopy = self.board.copy()
        res = []
        if isMaximazing:
            res.append(diagonala1(self.board, x, y, self.switch(isMaximazing)))
            res.append(diagonala2(self.board, x, y, self.switch(isMaximazing)))
            res.append(sloupec(self.board, x, y, self.switch(isMaximazing)))
            res.append(radek(self.board, x, y, self.switch(isMaximazing)))
            return max(res)
        else:
            res.append(diagonala1(self.board, x, y, self.switch(isMaximazing)))
            res.append(diagonala2(self.board, x, y, self.switch(isMaximazing)))
            res.append(sloupec(self.board, x, y, self.switch(isMaximazing)))
            res.append(radek(self.board, x, y, self.switch(isMaximazing)))
            return max(res)*-1

def diagonala1(list, x, y, hrac): # stejn?? princip hled??n??, ale kouk?? se ze sm??ru SZ-JV
    count = 0
    for i in range(1,5):
        if (x+i <= 14 and y+i <= 14):
            if (hrac==list[y+i][x+i]):
                count += 1
            else:
                break
    for i in range(1,5):
        if (x-i >= 0 and y-i >= 0):
            if (hrac==list[y-i][x-i]):
                count += 1
            else:
                break
    if (count >= 4):
        return True
    return count    

def diagonala2(list, x, y, hrac): # stejn?? princip hled??n??, ale kouk?? se ze sm??ru SV-JZ
    count = 0 
    for i in range(1,5):
        if (x-i >= 0 and y+i <= 14):
            if (hrac==list[y+i][x-i]):
                count += 1
            else:
                break
    for i in range(1,5):
        if (x+i <= 14  and y-i >= 0):
            if (hrac==list[y-i][x+i]):
                count += 1
            else:
                break
    if (count >= 4):
        return True
    return count

def radek(list, x, y, hrac):
    count = 0 # po????tadlo X nebo O z??le???? na hr????i
    for i in range(1,5): # for loop, kter?? bude koukat na ose x (doprava)
        if (x+i <= 14): # tahle podm??nka je zde, abychom se neocitli mimo hrac?? plochu
            if (hrac==list[y][x+i]): # kouk?? do m??ho seznamu, kde se ukl??daj?? data o h??e
                # hr???? 1 m?? ??islo 1 a hr???? 2 ????slo 2 a podle toho se mi ukl??daj?? i v seznamu
                # pokud dan?? hr???? bude m??t vedle posledn??ho zahran??ho m??sta (jeho posledn??ho tahu) sv??j symbol
                count += 1 # po????tadlo zapo??te, ??e se vedle nach??z?? jeho symbol
            else:
                break # kdyby vedle posledn??ho zahran??ho m??sta nebyl jeho symbol, p??eru???? se hled??n??

    for i in range(1,5): # to sam??, jako naho??e, ale pro druh?? sm??r (doleva)
        if (x-i >= 0):
            if (hrac==list[y][x-i]):
                count += 1
            else:
                break
    if (count >= 4): # pokud na??el v??ce jak (nebo p??esn??) 4 symboly vedle sebe v??me, ??e vyhr??lS
        return True
    return count

def sloupec(list, x, y, hrac): # zde se opakuje p??esn?? to sam??, ale pro sloupec, tak??e kouk?? na osu y
    count = 0 
    for i in range(1,5):
        if (y+i <= 14):
            if (hrac==list[y+i][x]): # kouk?? na osu y
                count += 1
            else:
                break
    for i in range(1,5):
        if (y-i >= 0):
            if (hrac==list[y-i][x]):
                count += 1
            else:
                break
    if (count >= 4):
        return True
    return count
