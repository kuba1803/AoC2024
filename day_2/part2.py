numElem = 1000
levels = []
numSafeRaport = 0


def valid(levels):
    for j in range(1, len(levels)):
        if (abs(levels[j] - levels[j - 1]) < 1 or abs(levels[j] - levels[j - 1]) > 3):
            return j
        if (j > 1 and ((levels[j] < levels[j - 1] and levels[j - 1] > levels[j - 2]) or (
                levels[j] > levels[j - 1] and levels[j - 1] < levels[j - 2]))):
            return j

    return -1


for i in range(numElem):
    levels = list(map(int, input().split()))
    errorLevelIdx = valid(levels)
    if errorLevelIdx == -1:
        numSafeRaport += 1
    else:
        for j in range(max(errorLevelIdx - 2, 0), errorLevelIdx + 1):
            cp_levels = levels.copy()
            del cp_levels[j]
            if valid(cp_levels) == -1:
                numSafeRaport += 1
                break

print(numSafeRaport)
