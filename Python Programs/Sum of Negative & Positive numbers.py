# Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List

n=[1,2,3,-4,-7,-2,-1,6,8,9,7]
even=[]
odd=[]
negative=[]
sum=0
for i in n:
    if i>0:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    else:
        sum=sum+i
        negative.append(i)
print(even)
print(odd)
print(negative)
print(sum)

