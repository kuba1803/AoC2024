numElem = 6
level = []
lastValue = 0
numSafeRaport = 0
isRaportSafe = True

for i in range(numElem):
    level = list(map(int, input().split()))
    isRaportSafe = True
    for j in range(1, len(level)):
        if (abs(level[j] - level[j - 1]) < 1 or abs(level[j] - level[j - 1]) > 3):
            isRaportSafe = False
        if (j > 1 and ((level[j] < level[j - 1] and level[j - 1] > level[j - 2]) or (
                level[j] > level[j - 1] and level[j - 1] < level[j - 2]))):
            isRaportSafe = False
    if (isRaportSafe):
        numSafeRaport += 1

print(numSafeRaport)
