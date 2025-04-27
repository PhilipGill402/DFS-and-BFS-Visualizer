from Constants import *

class Solver:
    def __init__(self, board):
        self.board = board
        self.visited = [[False for j in range(YCELLS)] for i in range(XCELLS)]
        self.numRows = YCELLS
        self.numCols = XCELLS
        self.MAX_NEIGHBORS = 8
        self.order = [] 
    
    def isValidPos(self, x, y):
        return x >= 0 and x < self.numCols and y >= 0 and y < self.numRows

    def isVisited(self, x, y):
        return self.visited[y][x]

    def visit(self, x, y):
        self.visited[y][x] = True

    def process(self, x, y):
        self.order.append((x, y)) 

    def getNeighbors(self, x, y):
        neighbors = []
        count = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if (not (i == 0 and j == 0)):
                    newX = x + i
                    newY = y + j
                    if (self.isValidPos(newX, newY)):
                        neighbors.append((newX, newY))
        
        return neighbors 