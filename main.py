import pygame
from Constants import * 
from Board import *
from BFS import *
from DFS import *
import time

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
BFSpositions = []
DFSpositions = []


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
            board.changeVal(col, row, 0)
            setTarget = True
        elif ev.type == pygame.MOUSEBUTTONDOWN and not setStart:
            #sets the start position denoted by a "-2" in the array
            (col, row) = getPos(x, y)
            board.changeVal(col, row, -2)
            startX = col
            startY = row 
            setStart = True
            BFSsolver = BFS(gameBoard, startX, startY)
            DFSsolver = DFS(gameBoard, startX, startY)
            BFSpositions = BFSsolver.bfs()
            DFSpositions = DFSsolver.dfs() 
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_b and setStart:
                for x, y in BFSpositions:
                    counter += 1
                    board.changeVal(x, y, counter)
                    board.drawBoard(surface)
                    pygame.display.update()
                    time.sleep(0.15)
            elif ev.key == pygame.K_d and setStart:
                for x, y in DFSpositions:
                    counter += 1
                    board.changeVal(x, y, counter)
                    board.drawBoard(surface)
                    pygame.display.update()
                    time.sleep(0.15)
            

        pygame.display.update()