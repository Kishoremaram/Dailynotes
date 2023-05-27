def function1(n):
    if n==0:
        return 0
    return function1(n-1)+n

n=int(input("Enter n value: "))
total=function1(n)
print(total)



