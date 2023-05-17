"""
You are given an array arr of n integers. For each index i, you have to find the sum of all integers present in the array with a value less than arr[i].
"""
#, 71, 87, 36, 54, 31, 8, 56, 71, 35, 65, 23, 79, 68, 92, 85
listA = [82, 96, 44, 22, 56]
k = len(listA)
for i in range(k):
    listSum = []
    for j in range(k):
        if listA[j] < listA[i]:
            listSum.append(listA[j])
    print(f"Index No.{i}, Value: {listA[i]}, ListSum = {listSum}, Result: {sum(listSum)}")
    
class Challenge6:
    def run(list):
        # Body

c = new Challenge6()
c.run()