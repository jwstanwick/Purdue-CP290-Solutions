import sys

#COMMENT EXPLANATIONS
#In the for loop I use the format w to denote a small weight
#and W to denote a larger weight than the small weight

maxWeight = 0
numPairs = int(sys.stdin.readline())
firstRow = sys.stdin.readline().split()
firstRow = [int(i) for i in firstRow] #Convert to integer
secondRow = sys.stdin.readline().split()
secondRow = [int(i) for i in secondRow] #Convert to integer

weightHold = 0
weight = 0
weightHold2 = 0
weight2 = 0
for curWeight in firstRow:
    if weightHold < curWeight and weight == 0:
        #if the weight is 0 and the weightHold < curWeight, we should change the weight value
        #to the current weight because we need to match it, and the prior matches are coming up even
        weight = curWeight

    elif weightHold < curWeight and curWeight < weight:
        #If weightHold is < curWeight and curWeight is < weight then we know
        #That the weight is in the format wW, so we should change weightHold
        #To curWeight
        weightHold = curWeight

    elif curWeight == weight:
        #If curWeight is the weight (ww), then weight should be 0 because it is matched
        #With its counterpart (weightHold stays constant because that is the max)
        weight = 0

    elif weightHold < weight and weight < curWeight:
        #If the hold weight (always < or equal to weight)
        #Is < (NOT EQUAL) and weight < curWeight then iterate the weights to their
        #Respective values wW and W < w
        weightHold = weight
        weight = curWeight

for curWeight2 in secondRow:
    if weightHold2 < curWeight2 and weight2 == 0:
        weight2 = curWeight2
    elif weightHold2 < curWeight2 and curWeight2 < weight2:
        weightHold2 = curWeight2
    elif curWeight2 == weight2:
        weight2 = 0
    elif weightHold2 < weight2 and weight2 < curWeight2:
        weightHold2 = weight2
        weight2 = curWeight2

#We print weightHold not weight because weightHold is our maximum value
if weight == weight2 and weight > weightHold and weight > weightHold2:
    print(weight)
elif weightHold > weightHold2:
    print(weightHold)
else:
    print(weightHold2)

#CHANGELOG
#Submission 1: Initial Submission
#Submission 2: Changed the iteration technique from one array to just running through both arrays
#Submission 3: Changed the order of the operators (weight = curWeight should be first and then the others should test)
#Submission 4: Reinstantiated to one array and also increased efficiency