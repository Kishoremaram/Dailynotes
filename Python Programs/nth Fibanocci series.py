#nth fibonacci
n=10
a=[0,1]
for i in range(2,n):
    a.append(a[i-1]+a[i-2])
print(a)
b = int(input("enter nth fibo series: "))
print(a[b-1])

