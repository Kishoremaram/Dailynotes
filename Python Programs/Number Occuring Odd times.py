# Python Program to Find the Number Occurring Odd Number of Times in a List

l=[1,1,2,2,2,3,3,3,3,5,5,5,5,5,6,6,6,6,6,7]
list1=[]
list2=[]
for i in range(0,len(l)):
    count=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            count=count+1
    if count%2!=0:
        list1.append(l[i])
list2=list(set(list1))
print(list2)
for x in list1:
    if x not in list2:
        list2.append(x)
print(list2)