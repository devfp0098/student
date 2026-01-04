import pygame as p
import random as r
import time as t
from sys import exit

def getscore():
    global timer, playerscore
    now = int(t.time() - timer)
    if gameactive and not gameover:
        playerscore = now
    return playerscore

def makegrid():#call only once per game
    global griddict, grid2d, mines, gridlength
    grid2d = []
    griddict = {}
    mines = r.sample(range(0, gridlength**2), 20)#num of samples = number of mines

    for x in range(gridlength):
        temp = []
        for y in range(gridlength):
            if x*gridlength+y in mines:
                temp.append(-1)
            else:
                temp.append(0)
        grid2d.append(temp)

    for y in range(gridlength):
        for x in range(gridlength):
            if grid2d[y][x] != -1:
                minesnum = 0
                if y == 0:#top row
                    if x == 0:#topleft
                        if grid2d[y+1][x] == -1:
                            minesnum += 1
                        if grid2d[y][x+1] == -1:
                            minesnum += 1
                        if grid2d[y+1][x+1] == -1:
                            minesnum += 1
                    elif x == gridlength-1:#topright
                        if grid2d[y+1][x] == -1:
                            minesnum += 1
                        if grid2d[y][x-1] == -1:
                            minesnum += 1
                        if grid2d[y+1][x-1] == -1:
                            minesnum += 1
                    else:#rest
                        if grid2d[y][x-1] == -1:
                            minesnum += 1
                        if grid2d[y+1][x-1] == -1:
                            minesnum += 1
                        if grid2d[y+1][x] == -1:
                            minesnum += 1
                        if grid2d[y+1][x+1] == -1:
                            minesnum += 1
                        if grid2d[y][x+1] == -1:
                            minesnum += 1
                elif x == 0:#left column
                    if y == gridlength-1:#bottomleft
                        if grid2d[y-1][x] == -1:
                            minesnum += 1
                        if grid2d[y-1][x+1] == -1:
                            minesnum += 1
                        if grid2d[y][x+1] == -1:
                            minesnum += 1
                    else:#rest
                        if grid2d[y-1][x] == -1:
                            minesnum += 1
                        if grid2d[y-1][x+1] == -1:
                            minesnum += 1
                        if grid2d[y][x+1] == -1:
                            minesnum += 1
                        if grid2d[y+1][x+1] == -1:
                            minesnum += 1
                        if grid2d[y+1][x] == -1:
                            minesnum += 1
                elif y == gridlength-1:#bottom row
                    if x == gridlength-1:#bottomright
                        if grid2d[y][x-1] == -1:
                            minesnum += 1
                        if grid2d[y-1][x-1] == -1:
                            minesnum += 1
                        if grid2d[y-1][x] == -1:
                            minesnum += 1
                    else:#rest
                        if grid2d[y][x-1] == -1:
                            minesnum += 1
                        if grid2d[y-1][x-1] == -1:
                            minesnum += 1
                        if grid2d[y-1][x] == -1:
                            minesnum += 1
                        if grid2d[y-1][x+1] == -1:
                            minesnum += 1
                        if grid2d[y][x+1] == -1:
                            minesnum += 1
                elif x == gridlength-1:#right column
                    if grid2d[y+1][x] == -1:
                        minesnum += 1
                    if grid2d[y+1][x-1] == -1:
                        minesnum += 1
                    if grid2d[y][x-1] == -1:
                        minesnum += 1
                    if grid2d[y-1][x-1] == -1:
                        minesnum += 1
                    if grid2d[y-1][x] == -1:
                        minesnum += 1
                else:
                    if grid2d[y-1][x-1] == -1:
                        minesnum += 1
                    if grid2d[y-1][x] == -1:
                        minesnum += 1
                    if grid2d[y-1][x+1] == -1:
                        minesnum += 1
                    if grid2d[y][x+1] == -1:
                        minesnum += 1
                    if grid2d[y+1][x+1] == -1:
                        minesnum += 1
                    if grid2d[y+1][x] == -1:
                        minesnum += 1
                    if grid2d[y+1][x-1] == -1:
                        minesnum += 1
                    if grid2d[y][x-1] == -1:
                        minesnum += 1
                grid2d[y][x] = minesnum
    
    count = 0
    for row in grid2d:
        for item in row:
            griddict[count] = [item, 'True']
            count += 1

def leftclick(mousecoord):
    if mousecoord[1] > gridlength*50:
        return 'pass'
    
    cellcoord = [mousecoord[0]//50, mousecoord[1]//50]
    for index in range(2):
        if cellcoord[index] == gridlength:
            cellcoord[index] == gridlength-1
    
    cellindex = (cellcoord[1] * gridlength) + cellcoord[0]
    global griddict
    if cellindex in flaggedindexes:
        rightclick(mousecoord)
        return 'pass'
    elif griddict[cellindex][0] == -1:
        return revealbombs()
    else:
        expandfrom(cellindex)

def expandfrom(index):
    global griddict
    if not griddict[index][1]:
        return 'pass'
    elif griddict[index][0] == -1:
        return 'pass'
    if index in flaggedindexes:
        return 'pass'
    elif griddict[index][0] > 0:
        griddict[index][1] = False
        return 'pass'
    else:
        griddict[index][1] = False
    
    proximities = []
    if index <= gridlength-1:#top row
        if index == 0:#topleft
            proximities.extend([index+1, index+gridlength, index+gridlength+1])
        elif index == gridlength-1:#topright
            proximities.extend([index-1, index+gridlength-1, index+gridlength])
        else:
            proximities.extend([index-1, index+1, index+11, index+12, index+13])
    elif index%gridlength == 0:#left col
        if index == gridlength*(gridlength-1):#bottomleft
            proximities.extend([index-gridlength, index-gridlength+1, index+1])
        else:
            proximities.extend([index-gridlength, index-gridlength+1, index+1, index+gridlength+1, index+gridlength])
    elif index > gridlength*(gridlength-1):#bottom row
        if index == gridlength**2-1:#bottomright
            proximities.extend([index-gridlength-1, index-gridlength, index-1])
        else:
            proximities.extend([index-1, index-gridlength-1, index-gridlength, index-gridlength+1, index+1])
    elif index%gridlength == gridlength-1:#right col
        proximities.extend([index-gridlength-1, index-gridlength, index+gridlength, index+gridlength-1, index-1])
    else:#rest
        proximities.extend([index-gridlength-1, index-gridlength, index-gridlength+1, index+1, index+gridlength+1, index+gridlength, index+gridlength-1, index-1])
    
    for indexes in proximities:
        expandfrom(indexes)

def blitgridstate():
    for y in range(gridlength):
        for x in range(gridlength):
            index = y*gridlength + x
            cellrect = cell.get_rect(topleft = (x*50+2, y*50+2))
            squarerect = square.get_rect(topleft = (x*50, y*50))
            if griddict[index][1]:#if covered
                p.draw.rect(screen, (220, 220, 220), cellrect, border_radius=3)
                if index in flaggedindexes:#if flag
                    screen.blit(flag, cellrect)
            else:#if revealed
                if griddict[index][0] != -1:#if not mine
                    numbersurf = font.render(f'{griddict[index][0]}', False, (255, 255, 255))
                    numberrect = numbersurf.get_rect(center = cellrect.center)
                    if not (x+y)%2:#if both are odd or if both are even (creates chequered grid)
                        p.draw.rect(screen, (43, 43, 43), squarerect)
                    else:
                        p.draw.rect(screen, (58, 58, 58), squarerect)
                    screen.blit(numbersurf, numberrect)
                else:#if mine
                    screen.blit(mine, cellrect)

def rightclick(mousecoord):
    global flaggedindexes, remainingflags
    if mousecoord[1] > gridlength*50:
        return 'pass'
    if remainingflags <= 0:
        return 'pass'
    
    cellcoord = [mousecoord[0]//50, mousecoord[1]//50]
    for index in range(2):
        if cellcoord[index] == gridlength:
            cellcoord[index] == gridlength-1
    
    cellindex = (cellcoord[1] * gridlength) + cellcoord[0]
    if not griddict[cellindex][1]:
        return 'pass'
    else:
        if cellindex in flaggedindexes:#remove flag
            flaggedindexes.remove(cellindex)
            remainingflags += 1
        else:
            flaggedindexes.append(cellindex)
            remainingflags -= 1

def revealbombs():
    global gameover
    gameover = True
    for index in griddict.keys():
        if index in mines:
            griddict[index][1] = False

def checkwin():
    safecells = [n for n in griddict.keys() if n not in mines]
    cellsleft = [n for n in safecells if griddict[n][1]]
    if len(cellsleft) == 0:
        revealbombs()
    
p.init()
screen = p.display.set_mode((600, 700))
screen.fill((43, 43, 43))
p.display.set_caption('Minesweeper')
clock = p.time.Clock()
gridlength = 12#change according to grid size (+change screen size accordingly)
cell = p.Surface((46, 46))
square = p.Surface((50, 50))
gameactive = False
gameover = False
remainingflags = 20#change according to number of mines
flaggedindexes = []
timer = t.time()
playerscore = 0

#text
font = p.font.Font('graphics/fonts/arialbold.ttf', 25)
titlefont = p.font.Font('graphics/fonts/arialbold.ttf', 75)
minifont = p.font.Font('graphics/fonts/arialbold.ttf', 10)
flagsurf = font.render(f'      Flags remaining: {remainingflags}', False, (255, 255, 255))
flagrect = flagsurf.get_rect(midleft = (0, 650))
scoresurf = font.render(f'                  Time:  {getscore()}', False, (255, 255, 255))
scorerect = scoresurf.get_rect(midleft = (300, 650))
titlesurf = titlefont.render('MINESWEEPER', False, (255, 255, 255))
titlerect = titlesurf.get_rect(midtop = (300, 50))
playtextsurf = font.render('Click to play', False, (255, 255, 255))
playtextrect = playtextsurf.get_rect(center = (300, 625))
gameovertext = font.render('GAMEOVER!', False, (43, 43, 43))
gameovertextrect = gameovertext.get_rect(midleft = (100, 650))
playagaintext = minifont.render('[ Click to return ]', False, (255, 255, 255))
playagainrect = playagaintext.get_rect(midbottom = (300, 690))
exittext = minifont.render('[ Right - click to exit ]', False, (255, 255, 255))
exittextrect = exittext.get_rect(midtop = (300, 675))

#images
mine = p.image.load('graphics/minesweeper/mine.png').convert_alpha()
mine = p.transform.scale(mine, (50, 50))
minelogosurf = p.transform.scale(mine, (400, 400))
minelogorect = minelogosurf.get_rect(midtop = (300, 200))
flag = p.image.load('graphics/minesweeper/flag.png').convert_alpha()
flag = p.transform.scale(flag, (50, 50))

makegrid()
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            exit()
        if gameactive:#main loop
            if not gameover:
                if event.type == p.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        leftclick(p.mouse.get_pos())
                    elif event.button == 3:
                        rightclick(p.mouse.get_pos())
            else:
                if event.type == p.MOUSEBUTTONDOWN and event.button in (1, 3):
                    gameactive = False
        else:#gameover loop
            if event.type == p.MOUSEBUTTONDOWN:
                if event.button == 1:#reset
                    gameactive = True
                    gameover = False
                    remainingflags = 20#change according to number of mines
                    flaggedindexes = []
                    timer = t.time()
                    playerscore = 0
                    makegrid()
                elif event.button == 3:
                    p.quit()
                    exit()
    screen.fill((43, 43, 43))
    checkwin()
    if gameactive:
        if not gameover:
            flagsurf = font.render(f'      Flags remaining: {remainingflags}', False, (255, 255, 255))
            flagrect = flagsurf.get_rect(midleft = (0, 650))
            scoresurf = font.render(f'                  Time:  {getscore()}', False, (255, 255, 255))
            scorerect = scoresurf.get_rect(midleft = (300, 650))
            screen.blit(flagsurf, flagrect)
            screen.blit(scoresurf, scorerect)
            blitgridstate()
        else:
            p.draw.rect(screen, (255, 255, 255), gameovertextrect)
            screen.blit(gameovertext, gameovertextrect)
            screen.blit(playagaintext, playagainrect)
            scoresurf = font.render(f'                  Time:  {getscore()}', False, (255, 255, 255))
            scorerect = scoresurf.get_rect(midleft = (300, 650))
            screen.blit(scoresurf, scorerect)
            blitgridstate()

    else:
        screen.blit(minelogosurf, minelogorect)
        screen.blit(playtextsurf, playtextrect)
        screen.blit(titlesurf, titlerect)
        screen.blit(exittext, exittextrect)
    p.display.update()
    clock.tick(60)