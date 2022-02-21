# Input

# Input contains up to 1000 test cases, one test case per line. Each line has three space-separated numbers: r m c, where 0<r≤1000 is a real number with at most 5 digits past the decimal indicating the true radius of the circle, 1≤m≤100000 is an integer indicating the total number of marked points, and 0≤c≤m is an integer indicating the number of marked points that fall in the circle. Input ends with a line containing three zeros, which should not be processed.

# Output

# For each test case, print a line containing two numbers: the true area of the circle and the estimate according to the experiment. Both numbers may have a relative error of at most 10^−5.

# The ratio of the area of a square to a circle of maximum area inscribed inside it is exactly 4:pi.  As we increase the number of dots we effectively increase our "resolution", getting closer and closer to the real value of pi.

import math
import sys

for line in sys.stdin:
    newLine = line.split()
    r = float(newLine[0])
    m = int(newLine[1])
    c = int(newLine[2])
    if r == 0:
        break

    trueArea = (r*r)*math.pi
    areaSquare = (r*2)*(r*2)
    estimateArea = areaSquare * (c/m)

    print(str(round(trueArea,9)) + " " + str(round(estimateArea,9)))