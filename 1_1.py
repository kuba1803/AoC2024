listA = []
listB = []
numElem = 1000
distance = 0


for i in range(numElem):
    pair = input().split()
    listA.append(int(pair[0]))
    listB.append(int(pair[1]))

listA.sort()
listB.sort()

for i in range(numElem):
    distance += abs(listA[i] - listB[i])

print(distance)