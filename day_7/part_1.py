import math
sum =0

with open('input.txt') as f:
    for line in f:
        vals = line.strip().split(": ")
        target = int(vals[0])
        parts = list(map(int, vals[1].split(" ")))
        numCombinatiuon = 3**(len(parts) -1)

        print( target )
        for i in range(numCombinatiuon):
            temp = parts[0]
            for j in range(1,len(parts)):
                if( i%3==0):
                    temp += parts[j]
                elif( i%3==1):
                    temp *= parts[j]
                else:
                    temp = int(str(temp) + str(parts[j]))
                i = math.floor(i / 3)

            if( temp == target ):
                sum += int(target)
                break

    print(sum)