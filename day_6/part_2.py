
map = []
mask = []
oTab = []
posX, posY = 0, 0
sum = 0

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

def appliedMove(map, mask,posY, posX, dir):
    mask[posY][posX] |= getDirMask(dir)
    map[posY][posX] = dir

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
        nextY, nextX = nextPosition( posY, posX, nextDir)
        if( nextY < 0 or nextY >= len(loopMap) or nextX < 0 or nextX >= len(loopMap[nextY])):
            break

        if( loopMap[nextY][nextX]=="#"):
            nextDir = changeDirection(nextDir)
            nextY, nextX = posY, nextX

        if( nextY < 0 or nextY >= len(loopMap) or nextX < 0 or nextX >= len(loopMap[nextY])):
            break

        if(checkRepeatStep(loopMask,nextY,nextX,nextDir)):
            print("curPosX", curPosX, "curPosY", curPosY, "dir", dir)
            print("loopPosX", loopPosX, "loopPosY", loopPosY)
            for i in range(len(loopMap)):
                print(loopMap[i])
            otab[loopPosY][loopPosX] = 1
            return True

        appliedMove(loopMap, loopMask, nextY, nextX, nextDir)
        if (nextY != posY or nextX != posX):
            loopMap[posY][posX] = "."
        posX = nextX
        posY = nextY

    return False


with open('input_example.txt') as f:
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

        appliedMove(map, mask, nextY, nextX, nextDir)
        if(nextY!=posY or nextX!=posX):
            map[posY][posX] = "."
        posX = nextX
        posY = nextY

for y in range(len(map)):
    for x in range(len(map[y])):
        sum+=oTab[y][x]

print(sum)
for y in range(len(map)):
    print(map[y])

for y in range(len(mask)):
    print(mask[y])

for y in range(len(oTab)):
    tab = []
    for x in range(len(oTab[y])):
        if( map[y][x]=="#"):
            tab.append("#")
        elif(oTab[y][x]==1):
            tab.append("O")
        elif((mask[y][x]&1==1 or mask[y][x]&4==4)and(mask[y][x]&2==2 or mask[y][x]&8==8) ):
            tab.append("+")
        elif(mask[y][x]&1==1 or mask[y][x]&4==4):
            tab.append("|")
        elif(mask[y][x]&2==2 or mask[y][x]&8==8):
            tab.append("-")
        else:
            tab.append(".")
    print(tab)

print(mask[1][4]&1)
print((mask[1][4]&2==1 or mask[1][4]&8==1))
