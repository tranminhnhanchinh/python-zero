class Solution:
    def findNumber(self, N : int) -> int:
        def help(n):
            if(n<6):return n+(n-1)
            if(n%5 == 0):return ((help((n//5) - 1))*10) + 9
            else:return (help(n//5)*10) + (n%5)+(n%5)-1
        return help(N)

