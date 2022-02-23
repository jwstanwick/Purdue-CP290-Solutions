import sys
import math
import time

fl = sys.stdin.readline().split()
numInvest = int(fl[0])
minAmt = int(fl[1])

lowDay = 0
highDay = 2*(10**9)
maxDay = 2*(10**9)
curDay = math.floor((highDay-lowDay)/2)
investArr = []
totalDayProfit = 0
totalDayCost = 0

for i in range(numInvest):
    line = sys.stdin.readline().split()
    investArr.append([int(line[0]), int(line[1])])
    # Daily Profit / Initial Cost
prevCurDay = curDay
while highDay-lowDay != 1:
    for i in investArr:
        if (i[0]*curDay)-i[1] > 0:
            totalDayProfit = totalDayProfit + i[0]*curDay
            totalDayCost = totalDayCost + i[1]
    if totalDayProfit-totalDayCost >= minAmt:
        highDay = curDay
        if math.floor((highDay-lowDay)/2):
            curDay = math.floor((highDay-lowDay)/2)
    else:
        lowDay = curDay
        if math.floor((highDay-curDay)/2):
            curDay = curDay + math.floor((highDay-curDay)/2)
        
    # print('totalDay Cost -> ' + str(totalDayCost))
    # print('totalDay Profit -> ' + str(totalDayProfit))

    totalDayProfit = 0
    totalDayCost = 0

    # print('highDay -> ' + str(highDay))
    # print('lowDay -> ' + str(lowDay))
    # print('curDay -> ' + str(curDay))
    # print('')
    # time.sleep(0.2)

totalDayProfit = 0
totalDayCost = 0
for i in investArr:
    if (i[0]*lowDay)-i[1] > 0:
        totalDayProfit = totalDayProfit + i[0]*lowDay
        totalDayCost = totalDayCost + i[1]

if totalDayProfit-totalDayCost >= minAmt:
    print(lowDay)
else:
    print(highDay)