# Given an integer S, write a program to print the square of size S using * character. 
""" s = int(input("Type: "))
def square(s):
    for i in range(s):
        if i == 0:
            print("* " * s)
        elif i > 0 and i < s-1:
            print("*", " "*(2*s-5), "*")
        else:
            print("* " * s)

square(s) """

#Print Square Wall 2
""" def printWall2(s):
    for i in range(5):
        for j in range(5):
            print("*", end = " ")
        print("")
printWall2(10) """

#Given an integer s. Write a program to print the Right angle triangle wall. The length of perpendicular and base is s.  Use single loop and string multiplication.
# Easy <<
#Right Angle Triangle 2
def Angle(s):
    for i in range(0, s):
        if i == 0:
            print("*")
        elif i> 0 and i <s-1:
            print("*"," "*(i-1)*2, "*")
        else:
            print("* "* s, end ="")
            
Angle(5)

## Solve problems in greeksforgreeks