#print first ten prime numbers square and sum of all those squares
n=100
sum=0
count = 0
k = int(input("enter of prime numbers count:"))
for i in range(2,n):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i,end=" ")
        x=i**2
        print(x)
        sum+=x
        count+=1
        if(count == k):
            break
print(sum)
