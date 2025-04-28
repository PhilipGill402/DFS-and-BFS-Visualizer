from Solver import *
from collections import deque

class DFS(Solver):
    def __init__(self, board, startX: int, startY: int):
        super().__init__(board)
        self.startX = startX
        self.startY = startY
    
    def dfs(self) -> list:
        stack = deque()
        super().visit(self.startX, self.startY)
        stack.append((self.startX, self.startY))
        while (len(stack) > 0):
            x, y = stack.pop()
            if self.board[y][x].value == 0:
                return self.order
            if (x, y) != (self.startX, self.startY):
                super().process(x, y)
            neighbors = super().getNeighbors(x, y)
            for nx, ny in neighbors:
                if (not super().isVisited(nx, ny)):
                    super().visit(nx, ny)
                    stack.append((nx, ny)) 
