# Game Of Subsets
"""
Elena is the topper of the class. Once her teacher asked her a problem. He gave Elena an array of integers of length n. 
He calls a subset of array arr good if its product can be represented as a product of one or more distinct prime numbers. 
He asked her to find the number of different good subsets in arr modulo 109 + 7.
Constraints:

1 <= N <= 10^5
1< = arr[i] <= 30
"""
""" import random
listRandom = []
for i in range(100):
    x = random.randrange(1, 30)
    listRandom.append(x)
print(listRandom) """
listA = [1, 2, 3, 4]
import json
listPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
listOK = []
for each in listA:
    listCheck = []
    if each == 1:
        listOK.append(each)
    else:
        for i in range(1, each+1):
            if i==1 or each % i == 0 and i in listPrime:
                listCheck.append(i)
    k = 1
    for m in listCheck:
        k *= m
    if k == each and k != 1:
        listOK.append(each)
k = len(listOK)
Pairlist = [(10, 14), (13, 26), (14, 26)]
import itertools
import math
import re

myList = []
for i in range(1, k):
    x = itertools.combinations(listOK, i)
    listM = list(x)
    print(listM)
    l = len(listM)
    for m in range(l):
        listX = list(itertools.combinations(listM[m], 2))
        for j in range(len(listX)):
            gcd = math.gcd(listX[j][0], listX[j][1])
            if gcd > 1:
                break
            else:
                myList.append(listM[m])
print(myList)
                

        