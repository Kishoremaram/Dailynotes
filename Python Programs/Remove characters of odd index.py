# Program to remove the characters of odd index values in a string
str1="helloteam"
res=""
for i in range(len(str1)):
    if i%2==0:
        res=res+str1[i]
print("removed odd Characters:",res)