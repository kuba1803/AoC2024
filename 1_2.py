listA = []
dictB = {}
numElem = 1000
distance = 0


for i in range(numElem):
    pair = input().split()
    listA.append(int(pair[0]))
    dictB[int(pair[1])] = dictB.get(int(pair[1]),0) + 1

for i in range(numElem):
    distance += listA[i] * dictB.get(listA[i],0)

print(distance)