
map = []
mask = []
maxX, maxY = 0, 0
posX, posY = 0, 0

with open('input_example.txt') as f:
    for line in f:
        maxY +=1
        maxX = max(maxX, len(line))
        map.append(line.strip())
        mask.append([0]*len(line))

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '^' or map[y][x] == 'v' or map[y][x] == '>' or map[y][x] == '<':
                posX = x
                posY = y

    while posX <= maxX and posY <= maxY and posX >=0 and posY >= 0:
        mask[posY][posX] = 1;
        print( "posX:", posX, "posY:", posY)
        if map[posY][posX] == '^':
            posY-=1
        elif map[posY][posX] == 'v':
            posY+=1
        elif map[posY][posX] == '>':
            posX+=1
        elif map[posY][posX] == '<':
            posX-=1

    for y in range(maxY):
        for x in range(maxX):
            if mask[y][x] == 1 :
                sum+=1


print(sum)
print(map)
print(mask)
