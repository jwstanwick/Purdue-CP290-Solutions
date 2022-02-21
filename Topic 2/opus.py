import sys

# This organizes the input into an array that can be manipulated
c = 0
falcArray=[]
numFalc = sys.stdin.readline()
numFalc = int(numFalc)
opusNum = sys.stdin.readline()
opusNum = opusNum.split()

for i in opusNum:
    opusNum[c] = int(i)
    falcArray.append(c+1)
    c = c+1
    
c = 0
curOpus = opusNum[0]
startIndex = 0

while len(falcArray) > 2:
    while curOpus > len(falcArray):
        curOpus = curOpus - len(falcArray)

    delIndex = curOpus-1
    falcArray.pop(delIndex)
    opusNum.pop(delIndex)

    if delIndex > len(opusNum)-1:
        curOpus = opusNum[0]
        curProf = falcArray[0]
    else: 
        curOpus = opusNum[delIndex] + delIndex
        curProf = falcArray[delIndex]

if curOpus % 2 == 1:
    print(falcArray[1])
else:
    print(falcArray[0])