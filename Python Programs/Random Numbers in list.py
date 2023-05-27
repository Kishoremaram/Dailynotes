#program to take random numbers in list
import random
a=[]
x=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    b=random.randint(1,20)
    if b not in a:
        a.append(b)
    else:
        x.append(b)
print('Randomised list is: ',a)
print('duplicate list is: ',x)
