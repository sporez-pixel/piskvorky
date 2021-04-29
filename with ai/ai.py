# algorithm - minimax
from vyhra import *
from random import randint

class computer:
    def __init__(self):
        pass
    
    def minimax(self, depth, isMaximazing, lastMoves):

        someonewon = vyhra(self.board, lastMoves[0], lastMoves[1], switch(isMaximazing))
        if someonewon and isMaximazing:
            return 1
        elif someonewon:
            return -1

        if depth<0:
            return 0
        
        if (isMaximazing):
            bestScore = -100
            for y in range(15):
                for x in range(15):
                    if self.possible(x,y):
                        self.board[y][x] = 2
                        score = self.minimax(depth-1, False, [x,y])
                        self.board[y][x] = 0
                        bestScore = max([score,bestScore])
            return bestScore

        else:
            bestScore = 100
            for y in range(15):
                for x in range(15):
                    if self.possible(x,y):
                        self.board[y][x] = 1
                        score = self.minimax(depth-1, True, [x,y])
                        self.board[y][x] = 0
                        bestScore = max([score,bestScore])
            return bestScore

    def getBoard(self, board):
        self.board = board

    def computerMove(self):
        possible = False
        while(possible == False):
            x,y = self.randomMove()
            possible = self.possible(x,y)
        return x,y

    def searchMoves(self):
        pass

    def randomMove(self):
        x = randint(0,14)
        y = randint(0,14)
        return x,y

    def possible(self,x,y):
        if self.board[y][x] == 0:
            return True
        return False

    def switch(self, bool):
        if bool:
            return 2
        return 1