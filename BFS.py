from Solver import *
from collections import deque

class BFS(Solver):
    def __init__(self, board, startX: int, startY: int):
        super().__init__(board)
        self.startX = startX
        self.startY = startY
    
    def bfs(self):
        queue = deque()
        super().visit(self.startX, self.startY)
        queue.append((self.startX, self.startY))
        while (len(queue) > 0):
            x, y = queue.popleft()
            neighbors = super().getNeighbors(x, y)
            for i in neighbors:
                x = i[0]
                y = i[1]
                if (not super().isVisited(x, y)):
                    if self.board[y][x].value == 0:
                        break
                    super().visit(x, y)
                    super().process(x, y)
                    queue.append(i)