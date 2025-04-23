import pygame
from Constants import YCELLS, XCELLS, WIDTH, HEIGHT, WHITE
from Square import *

class Board:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def createBoard(self) -> list:
        board = []
        for i in range(YCELLS):
            board.append([])
            for j in range(XCELLS):
                board[i].append(Square())

        return board

    
    def drawBoard(self, surface: pygame.surface) -> None:
        for i in range(YCELLS):
            for j in range(XCELLS):
                width = int(WIDTH / XCELLS)
                height = int(HEIGHT / YCELLS)
                x = j * width
                y = i * height
                if self.board[i][j]:
                    pygame.draw.rect(surface, WHITE, (x,y,width,height))
                else:
                    pygame.draw.rect(surface, WHITE, (x,y,width,height), 1, border_radius=1)
    
    def changeVal(self, x:int, y:int, val:bool) -> None:
        self.board[y][x] = val