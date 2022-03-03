#Author: John Stanwick
#It is ok to show this solution to others

import sys
import math

fl = sys.stdin.readline().split()
numInvest = int(fl[0])
minAmt = int(fl[1])

#To solve this, we must instiantiate the highest and lowest days possible to solve
lowDay = 0
highDay = 2*(10**9)
curDay = math.floor((highDay-lowDay)/2)
investArr = []
totalDayProfit = 0
totalDayCost = 0

#Input
for i in range(numInvest):
    line = sys.stdin.readline().split()
    investArr.append([int(line[0]), int(line[1])])

prevCurDay = curDay
while highDay-lowDay != 1: #While the range of days that we are looking at are not adjacent days
    #Find if an investment is optimal for a given day
    for i in investArr:
        if (i[0]*curDay)-i[1] > 0:
            totalDayProfit = totalDayProfit + i[0]*curDay
            totalDayCost = totalDayCost + i[1]

    #Find whether to move the range of days to calculate for
    if totalDayProfit-totalDayCost >= minAmt:
        highDay = curDay
        if math.floor((highDay-lowDay)/2):
            curDay = math.floor((highDay-lowDay)/2)
    else:
        lowDay = curDay
        if math.floor((highDay-curDay)/2):
            curDay = curDay + math.floor((highDay-curDay)/2)

    #Reset variables
    totalDayProfit = 0
    totalDayCost = 0

#Calculate for the last two days
totalDayProfit = 0
totalDayCost = 0
for i in investArr:
    if (i[0]*lowDay)-i[1] > 0:
        totalDayProfit = totalDayProfit + i[0]*lowDay
        totalDayCost = totalDayCost + i[1]

#Print depending upon the last calculation
if totalDayProfit-totalDayCost >= minAmt:
    print(lowDay)
else:
    print(highDay)