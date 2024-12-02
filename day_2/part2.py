numElem = 1000
levels = []
lastValue = 0
numSafeRaport = 0
isRaportSafe = True

def valid( levels ):
    errorLevelIdx = -1
    for j in range(1, len(levels)):
        if (abs(levels[j] - levels[j - 1]) < 1 or abs(levels[j] - levels[j - 1]) > 3):
            errorLevelIdx = j
            break
        if (j > 1 and ((levels[j] < levels[j - 1] and levels[j - 1] > levels[j - 2]) or (
                levels[j] > levels[j - 1] and levels[j - 1] < levels[j - 2]))):
            errorLevelIdx = j
            break

    return errorLevelIdx


for i in range(numElem):
    levels = list(map(int, input().split()))
    if valid(levels) == -1:
        numSafeRaport += 1
    else:
        for j in range(0, len(levels)):
            cp_levels = levels.copy()
            del cp_levels[j]
            if valid(cp_levels) == -1:
                numSafeRaport += 1
                break

print(numSafeRaport)