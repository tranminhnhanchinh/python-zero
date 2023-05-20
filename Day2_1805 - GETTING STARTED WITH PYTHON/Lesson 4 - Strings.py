#ord() ==> Change character to number
#chr() ==> change number to character

#String Operations Part (1)
"a" in "Nhan Chinh" #True
"A" in "Nhan Chinh" #False

#String Method
#1- Index() ==>  index of the first occurrence
# str.index("X") ==> Return index of the first "X" occurence in str
#2- rindex()
x = "Nhan Chinh"
# print(x.index("n"))
# print(x.rindex("n"))
#3- Start with method
print(x.startswith("nh")) #False
print(x.startswith("Nh")) #True
#4- endswith()
#5- Find()
print(x.find("nh")) #Return lowest index or first occurrence
print(x.find("XXXXX")) #Return -1 if not found