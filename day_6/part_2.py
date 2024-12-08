
map = []
mask = []
oTab = []
posX, posY = 0, 0
sum = 0

def printRead(map,mask,oTab):
    for y in range(len(oTab)):
        tab = []
        for x in range(len(oTab[y])):
            if (map[y][x] == "#"):
                tab.append("#")
            elif (oTab[y][x] == 1):
                tab.append("O")
            elif ((mask[y][x] & 1 == 1 or mask[y][x] & 4 == 4) and (mask[y][x] & 2 == 2 or mask[y][x] & 8 == 8)):
                tab.append("+")
            elif (mask[y][x] & 1 == 1 or mask[y][x] & 4 == 4):
                tab.append("|")
            elif (mask[y][x] & 2 == 2 or mask[y][x] & 8 == 8):
                tab.append("-")
            else:
                tab.append(".")
        print(tab)

def nextPosition( posY, posX, dir):
    if dir == '^':
        return posY - 1, posX
    if dir == '>':
        return posY, posX + 1
    if dir == 'v':
        return posY + 1, posX
    if dir == '<':
        return posY, posX - 1

def changeDirection( dir):
    if dir == '^':
        return ">"
    if dir == '>':
        return "v"
    if dir == 'v':
        return "<"
    if dir == '<':
        return "^"

def getDirMask(dir):
    if dir == '^':
        return 1
    if dir == '>':
        return 2
    if dir == 'v':
        return 4
    if dir == '<':
        return 8
    return 0

def checkRepeatStep(mask,posY, posX, dir):
    if((mask[posY][posX]&getDirMask(dir))==0):
        return False
    return True

def appliedMove(map, mask,posY, posX,nextY, nextX, dir, nextDir):
    mask[posY][posX] |= getDirMask(dir)
    map[nextY][nextX] = nextDir
    if (nextY != posY or nextX != posX):
        map[posY][posX] = "."

def checkLoop(map, mask, curPosY, curPosX, dir, otab):
    loopPosY, loopPosX = nextPosition(curPosY, curPosX, dir)
    if (loopPosY < 0 or loopPosY >= len(map) or loopPosX < 0 or loopPosX >= len(map[loopPosY])):
        return False
    if (map[loopPosY][loopPosX]== "#" or otab[loopPosY][loopPosX]== "1"):
        return False


    loopMap = []
    for i in range(len(map)):
        loopMap.append(map[i].copy())

    loopMask = []
    for i in range(len(map)):
        loopMask.append(mask[i].copy())

    loopMap[loopPosY][loopPosX] = "#"

    posY = curPosY
    posX = curPosX

    while True:
        nextDir = loopMap[posY][posX]

        if (checkRepeatStep(loopMask, posY, posX, nextDir)):
            otab[loopPosY][loopPosX] = 1
            return True

        nextY, nextX = nextPosition( posY, posX, nextDir)
        if( nextY < 0 or nextY >= len(loopMap) or nextX < 0 or nextX >= len(loopMap[nextY])):
            break

        if( loopMap[nextY][nextX]=="#"):
            nextDir = changeDirection(nextDir)
            nextY, nextX = posY, posX

        if( nextY < 0 or nextY >= len(loopMap) or nextX < 0 or nextX >= len(loopMap[nextY])):
            break

        appliedMove(loopMap, loopMask,posY,posX, nextY, nextX,loopMap[posY][posX], nextDir)
        posX = nextX
        posY = nextY

    return False


with open('input_file.txt') as f:
    for line in f:
        map.append(list(line.strip()))
        mask.append([0]*len(map[0]))
        oTab.append([0]*len(map[0]))

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '^' or map[y][x] == 'v' or map[y][x] == '>' or map[y][x] == '<':
                posX = x
                posY = y

    while True:
        nextDir = map[posY][posX]
        checkLoop(map, mask, posY, posX, nextDir, oTab)
        nextY, nextX = nextPosition( posY, posX, nextDir)
        if( nextY < 0 or nextY >= len(map) or nextX < 0 or nextX >= len(map[nextY])):
            break

        if( map[nextY][nextX]=="#"):
            nextDir = changeDirection(nextDir)
            nextY, nextX = posY, posX

        if( nextY < 0 or nextY >= len(map) or nextX < 0 or nextX >= len(map[nextY])):
            break

        appliedMove(map, mask,posY,posX, nextY, nextX,map[posY][posX], nextDir)
        posX = nextX
        posY = nextY

for y in range(len(map)):
    for x in range(len(map[y])):
        sum+=oTab[y][x]

print(sum)


printRead(map,mask,oTab)
