A = [2, 3, 3, 7, 15, 21, 23]
import itertools
B = itertools.combinations(A, 2)
print(list(B))
C = [(2, 3), (2, 3), (2, 7), (2, 15), (2, 21), (2, 23), (3, 7), (3, 23), (3, 7), (3, 23), (7, 15), (7, 23), (15, 23), (21, 23)]
D = C + A

