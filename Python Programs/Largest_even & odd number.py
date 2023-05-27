# Python Program to Print Largest Even and Largest Odd Number in a List
a=[1,2,3,5,6,7,8]
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
b.sort()
c.sort()
print(b[-1])
print(c[-1])