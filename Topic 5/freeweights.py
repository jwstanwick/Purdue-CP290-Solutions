#Author: John Stanwick
#It is ok to show this solution to others

#COMMENT EXPLANATIONS
#In the for loop I use the format w to denote a small weight
#and W to denote a larger weight than the small weight

import sys

maxWeight = 0
numPairs = int(sys.stdin.readline())
firstRow = sys.stdin.readline().split()
firstRow = [int(i) for i in firstRow]
secondRow = sys.stdin.readline().split()
secondRow = [int(i) for i in secondRow]

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
        #That the weight is in the format wW, so we should change weightHold to curWeight
        weightHold = curWeight

    elif curWeight == weight:
        #If curWeight is the weight (ww), then weight should be 0 because it is matched
        #With its counterpart (weightHold stays constant because that is the max)
        weight = 0

    elif weightHold < weight and weight < curWeight:
        #If the hold weight (always < or equal to weight) is < (NOT EQUAL) and weight < curWeight 
        #then iterate the weights to their respective values
        weightHold = weight
        weight = curWeight

#Repeat the loop for the second row
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

#We need this structure to account for if a weight's pair is on a different rack
if weight == weight2 and weight > weightHold and weight > weightHold2:
    print(weight)
elif weightHold > weightHold2:
    print(weightHold)
else:
    print(weightHold2)