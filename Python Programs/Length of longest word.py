# Python Program to Return the Length of the Longest Word from the List of Words

l=["apple","Banana","cat","rat","light"]
for i in range(0,len(l)-1):
    if len(l[i])>len(l[i+1]):
        temp=l[i]
        l[i]=l[i+1]
        l[i+1]=temp
print(len(l[-1]))