# Python Program to Find the Union of Two Lists

l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
for i in l2:
    if i not in l1:
        l1.append(i)
print(l1)
