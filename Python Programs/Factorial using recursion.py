#program to print factorial

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

x=int(input("Enter n value: "))
a=fact(x)
print(a)
