import pygame as p
import random as r
import time as t

def displayboard():
    global board
    for y in range(boardy):
        for x in range(boardx):
            cellcenter = (x*100+50, y*100+50)
            if board[y][x] == -1:
                p.draw.circle(gridsurf, (0, 0, 0), cellcenter, 37.5, 3)
            elif board[y][x] == 0:
                p.draw.circle(gridsurf, (0, 0, 0), cellcenter, 37.5, 3)
                p.draw.circle(gridsurf, (255, 0, 0), cellcenter, 35)
            else:
                p.draw.circle(gridsurf, (0, 0, 0), cellcenter, 37.5, 3)
                p.draw.circle(gridsurf, (0, 0, 255), cellcenter, 35)
p.init()
screen = p.display.set_mode((800, 700))
p.display.set_caption('Connect 4')
gridsurf = p.Surface((700, 600), p.SRCALPHA)
gridsurf.convert_alpha()
gridrect = gridsurf.get_rect(topleft = (50, 50))
p.draw.rect(screen, (43, 43, 43), gridrect, border_radius=10)


board = []
boardx = 7
boardy = 6
temp = []
for y in range(boardy):
    for x in range(boardx):
        temp.append([0 if (x+y)%2 else 1][0])
    board.append(temp)
    temp = []
displayboard()
screen.blit(gridsurf, gridrect)
p.display.flip()
clock = p.time.Clock()

t.sleep(5)