# algorithm - minimax
from vyhra import *
from random import randint

class computer:
    def __init__(self):
        pass
    
    def minimax(self, depth, isMaximazing):
        pass

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