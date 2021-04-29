# algorithm - minimax
from vyhra import *
from random import randint

class computer:
    def __init__(self):
        self.whatToCheck = [[1,1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1],[1,-1],[-1,1]]
    
    def minimax(self, depth, isMaximazing, lastMoves):
        someonewon = vyhra(self.board, lastMoves[0], lastMoves[1], self.switch(isMaximazing))
        if someonewon and isMaximazing:
            return 1

        if someonewon and (isMaximazing==False):
            return -1

        if depth<0:
            return 0
        
        if (isMaximazing):
            bestScore = -100
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
            bestScore = 100
            for l in self.whatToCheck:
                x = lastMoves[0]+l[0]
                y = lastMoves[1]+l[1]
                if self.possible(x,y):
                    self.board[y][x] = 2
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
        bestScore = -100
        for l in self.whatToCheck:
            x = lastMoves[0]+l[0]
            y = lastMoves[1]+l[1]
            if self.possible(x,y):
                self.board[y][x] = 2
                score = self.minimax(3, True, [x,y])
                self.board[y][x] = 0
                if score>bestScore:
                    bestScore = score
                    rx = x
                    ry = y
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