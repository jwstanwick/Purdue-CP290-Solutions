# Very similar to top-down, except instead of starting at the “top” of the problem and recursing into subproblems, we prefill the base case subproblems and iterate through larger and larger subproblems until we reach the final answer
# Basic steps to build bottom-up DP solution:

#     Determine the parameters that uniquely describe the problem (aka the state)
#     Create a container (eg. array) that has one entry per state (fib sequence: array of size n)
#         Only need to initialize with known initial values (fib[0] and fib[1], for example)
#     With base case states already filled, determine the next cells/states that can be filled in next (as defined by the transitions).  Repeat this process until the table is complete.
#         This usually occurs with loops


import sys
from weakref import finalize

numTrains = int(sys.stdin.readline())
trainArr = []
revTrainArr = []
for i in range(numTrains):
    x = int(sys.stdin.readline())
    trainArr.append(x)
    revTrainArr.insert(0, x)

dpArr = [1]*numTrains #We don't have to do two because we dont need to return the number of valid lengths
dpArr2 = [1]*numTrains

for i in range(numTrains):
    for x in range(i):
        if revTrainArr[i] > revTrainArr[x] and dpArr[i] < (dpArr[x] + 1):
            dpArr[i] = dpArr[x]+1
        if revTrainArr[i] < revTrainArr[x] and dpArr2[i] < (dpArr2[x] + 1):
            dpArr2[i] = dpArr2[x]+1

finalArr = [sum(x) for x in zip(dpArr, dpArr2)]

#I just know these edge cases are going to mess me up
if numTrains == 0:
    print(0)
elif numTrains == 1:
    print(1)
else:
    maxLen = max(finalArr) - 1
    print(maxLen)

#Changelog 1: Removed the reset counter switch
#Changelog 2: Added catch for adding to the back
#Changelog 3: Consolidated ifs
#Changelog 4: Debug with Ethan