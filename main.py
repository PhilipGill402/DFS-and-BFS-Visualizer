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
oldBoard = board.oldBoard
simRunning = False
setTarget = False
counter = 0

while running:
    surface.fill(BLACK)
    board.drawBoard(surface)
    (x,y) = pygame.mouse.get_pos()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.MOUSEBUTTONUP and not setTarget:
            (col, row) = getPos(x, y) 
            

        pygame.display.update()