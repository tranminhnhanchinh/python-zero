"""
Given an integer N, You need to find the Nth smallest number which only contains odd 
digits i.e. 1,3,5,7,9 means no even digits are allowed on that number (12 will not consider).
For example, the starting numbers which only contain odd digits are 1,3,5,7,9,11,13,15,17,19,31,33,35 and so on.
Explanation:
N=13
Output:
35
First 13 numbers are 1,3,5,7,9,
11,13,15,17,19,31,33,35, here 35 
is the answer.
You don't need to read input or print anything. 
Your task is to complete the function findNumber() which takes a single variable N and returns the smallest Nth
number which only contains odd digits.

"""

import re
listNumber = []
k = 1
i = 1
while k < 1000:
    i = int(i) + 2
    i = str(i)
    boolIt =[]
    for j in i:
        m = int(j) % 2
        if m == 0:
            boolIt.append(False)
        else:
            boolIt.append(True)
        
    if False in boolIt:
        pass
    else:
        listNumber.append(int(i))
        k += 1
print(listNumber)
#Test