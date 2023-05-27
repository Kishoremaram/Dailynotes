# Python Program to Sort a List According to the Second Element in Sublist
l=[[20,88],[57,18],[65,26],[13,84]]
for i in range(0,len(l)-1):
        if l[i][1] > l[i+1][1]:
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp
print(l)