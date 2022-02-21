import sys
import bisect

fl = sys.stdin.readline().split()
length = int(fl[0])
hei = int(fl[1])

botArr = [0] * int(length/2)
topArr = [0] * int(length/2)

for x in range(length):
    line = int(sys.stdin.readline())

    if x % 2 == 1:
        x = int((x/2)+0.5)-1
        topArr[x] = line
    else:
        x = int(x/2)
        botArr[x] = line

topArr.sort()
botArr.sort()

minCollisions = sys.maxsize
numLevels = 0
collisions = 0

for i in range(hei):
    collisions = 0
    i = i + 1

    botIndex = -1
    x = bisect.bisect_left(botArr, i)
    if x != len(botArr):
        botIndex = botArr[x]
        collisions = collisions + len(botArr) - botArr.index(botIndex)

    if collisions <= minCollisions:
        topIndex = -1
        z = bisect.bisect_right(topArr, hei-i)
        if z != len(topArr):
            topIndex = topArr[z]
            collisions = collisions + len(topArr) - topArr.index(topIndex)

        if collisions < minCollisions:
            minCollisions = collisions
            numLevels = 1
        elif collisions == minCollisions:
            numLevels = numLevels + 1

    # print('i value is ' + str(i))
    # print('the collisions are ' + str(collisions))
    # print('the min collisions are ' + str(minCollisions))
    # print()

print(str(minCollisions) + ' ' + str(numLevels))