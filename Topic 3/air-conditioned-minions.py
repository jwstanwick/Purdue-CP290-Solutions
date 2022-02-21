import sys

numMinions = int(sys.stdin.readline())
minArray = []

# This code is from a prior attempt in solving
# minTemp = 100000000
# maxTemp = -100000000

for i in range(numMinions):
    line = sys.stdin.readline()
    line = line.split()
    line[0] = int(line[0])
    line[1] = int(line[1])

    # This code is from a prior attempt in solving
    # if line[0] < minTemp:
    #     minTemp = line[0]
    # elif line[0] > maxTemp:
    #     maxTemp = line[0]

    # if line[1] > maxTemp:
    #     maxTemp = line[1]
    # elif line[1] < minTemp:
    #     minTemp = line[1]

    minArray.append([line[0],line[1]])

#This sorts the minion array by lower bound (thanks Shaun for the help!)
minArray.sort(key=lambda x: x[0])

z = 0
while len(minArray) != 0:
    z = z + 1
    lowerBound = minArray[0][0]
    upperBound = minArray[0][1]
    minArray.pop(0)
    while len(minArray) != 0 and ((lowerBound <= minArray[0][0] and minArray[0][0] <= upperBound) or (lowerBound <= minArray[0][1] and minArray[0][1] <= upperBound)):
        #I hate this while loop so much and there is probably
        #a way to consolidate it but I'm tired and the calc2 test has 
        #made me want to just perish from this earth so it stays
        if lowerBound < minArray[0][0]:
            lowerBound = minArray[0][0]
        if upperBound > minArray[0][1]:
            upperBound = minArray[0][1]
        minArray.pop(0)
print(z)