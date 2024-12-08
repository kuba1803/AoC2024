
map = []
mask = []
posX, posY = 0, 0
sum = 0

with open('input.txt') as f:
    for line in f:
        map.append(list(line.strip()))
        mask.append([0]*len(map[0]))

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '^' or map[y][x] == 'v' or map[y][x] == '>' or map[y][x] == '<':
                posX = x
                posY = y

    while posX <= len(map[0]) and posY < len(map) and posX >=0 and posY >= 0:
        mask[posY][posX] = 1;
        print( "posX:", posX, "posY:", posY, "dir:", map[posY][posX])
        if map[posY][posX] == '^':
            map[posY][posX]='.'
            if( posY <= 0 ):
                break
            elif (map[posY - 1][posX] == '#'):
                map[posY][posX] = '>'
            else:
                posY-=1
                map[posY][posX] = '^'
        elif map[posY][posX] == 'v':
            map[posY][posX]='.'
            if( posY + 1 >= len(map)):
                break
            elif( map[posY + 1][posX] == '#'):
                map[posY][posX] = '<'
            else:
                posY+=1
                map[posY][posX] = 'v'
        elif map[posY][posX] == '>':
            map[posY][posX]='.'
            if( posX + 1 >= len(map[0])):
                break
            elif( map[posY][posX+1] == '#'):
                map[posY][posX] = 'v'
            else:
                posX+=1
                map[posY][posX] = '>'
        elif map[posY][posX] == '<':
            map[posY][posX]='.'
            if( posX <= 0 ):
                break
            elif( map[posY][posX-1] == '#'):
                map[posY][posX] = '^'
            else:
                posX-=1
                map[posY][posX] = '<'
        else:
            break

        for y in range(len(map)):
            print(map[y])


    for y in range(len(map)):
        for x in range(len(map[0])):
            if mask[y][x] == 1 :
                sum+=1


print(sum)
for y in range(len(map)):
    print(map[y])

for y in range(len(mask)):
    print(mask[y])

