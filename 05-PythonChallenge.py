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
listA = [12, 1, 3, 3, 10, 13, 14, 14, 29, 26]
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
print(listOK)
k = len(listOK)
Pairlist = [(10, 14), (13, 26), (14, 26)]
import itertools
import math
import re
x = itertools.combinations(listOK, 2)
print(list(x))
z = Pairlist[1]



""" for i in range(1, k):
    x = itertools.combinations(listOK, i) """
    # 
    
    
    
    # print(list(x))
    