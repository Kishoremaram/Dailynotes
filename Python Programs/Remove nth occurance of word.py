Python Program to Remove the ith Occurrence of the Given Word in a List

a=["kishore","sarala","jagadish","kishore","laxman","kishore"]
print(a)
n=int(input("Enter ith occurance:"))
b=input("Enter word:")
count=0
for i in range(0,len(a)):
    if a[i]==b:
        count=count+1
        if count==n:
            del a[i]
            break
print(a)
