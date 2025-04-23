import pygame
from Constants import * 
import time
from Board import *

def getPos(x:int,y:int) -> tuple:
    return (int(x//SQUAREX), int(y//SQUAREY))

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Finding")
running = True
board = Board()
gameBoard = board.board
simRunning = False
setTarget = False
setStart = False
counter = 0

while running:
    surface.fill(BLACK)
    board.drawBoard(surface)
    (x,y) = pygame.mouse.get_pos()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.MOUSEBUTTONDOWN and not setTarget:
            #sets the target position denoted by a "0" in the array
            (col, row) = getPos(x, y)
            gameBoard[row][col].changeValue(0)
            setTarget = True
        elif ev.type == pygame.MOUSEBUTTONDOWN and not setStart:
            #sets the start position denoted by a "-2" in the array
            (col, row) = getPos(x, y)
            gameBoard[row][col].changeValue(-2)
            setStart = True
            

        pygame.display.update()