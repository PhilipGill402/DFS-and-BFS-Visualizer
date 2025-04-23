import pygame
from Constants import YCELLS, XCELLS, WIDTH, HEIGHT, WHITE
from Square import *

class Board:
    def __init__(self) -> None:
        self.board = self.createBoard() 

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
                square = self.board[i][j]
                if square.color == BLACK:
                    pygame.draw.rect(surface, WHITE, (x,y,width,height), 1, border_radius=1)
                else:
                    pygame.draw.rect(surface, square.color, (x,y,width,height))
    
    def changeVal(self, x:int, y:int, val:bool) -> None:
        self.board[y][x] = val