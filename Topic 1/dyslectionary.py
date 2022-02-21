import sys

nDict = []
revDict = []
finalDict = []
gatherWords = []
maxLen = 0

for line in sys.stdin:
    if(line != "\n"):
        #Append Words
        gatherWords.append(line.rstrip())
    else:
        for word in gatherWords:
            revWord = word[::-1]
            if len(word) > maxLen:
                maxLen = len(word)
            revDict.append(revWord)
        revDict.sort()

        #Reverse the sorted words
        for word in revDict:
            revWord = word[::-1]
            while len(revWord) < maxLen:
                revWord = ' ' + revWord
            finalDict.append(revWord)

        #Reset all of the variables
        maxLen = 0
        nDict = []
        revDict = []
        gatherWords = []
        finalDict.append("")

#Final iteration
for word in gatherWords:
    revWord = word[::-1]
    if len(word) > maxLen:
        maxLen = len(word)
    revDict.append(revWord)
revDict.sort()

#Reverse the sorted words
for word in revDict:
    revWord = word[::-1]
    while len(revWord) < maxLen:
        revWord = ' ' + revWord
    finalDict.append(revWord)

for word in finalDict:
    print(word)