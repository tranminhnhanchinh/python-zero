#1- Print Function
"""
print("Message", sep = " ", end = " ")
sep: What to separate the object, default: ""
end: What to print at the end, default: \n (New line)
"""

#2- String Literals (Chuoi ky tu)
"""
\n -> Newline
"""
print("My name is \nChinh")

#3- Variables
"""
var = "Chinh" --> str
var2 = 120.33 --> float
var3 = 39 --> int
var4 = True --> bool
var5 = 12 + 3j --> complex
"""
#4- Input Function
"""
name = input("What is your name? \n")

"""
# name = input("What is your name? \n")
#5- Operator
"""
+ Addition
- Subtraction
* Multiplication
/ Division
// Division (floor)
% Modulus
** Power
"""
#6- Type Conversion
"""
float(a)
int(a)
list(a)
tuple(a)
set(a)
str(a)
ord() ==> Chuyen ky tu thanh so nguyen
chr() ==> Chuyen so thanh ky tu
hex() ==> Chuyen so nguyen thanh so he thap luc phan
oct() ==> Chuyen so nguyen thanh so he bat phan
"""
print(ord("B"))
print(chr(100))

#7- Comment
# Online
"""
    Multiple lines
"""

#8- If, Else, Elif
a = 5
if a > 1:
    print("A is greater than 1")
# This is performed and end!
elif a is int:
    print("A is int")
else:
    print("Unknown A")
