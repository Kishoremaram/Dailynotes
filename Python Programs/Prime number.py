#Program for prime number
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print(n,"is not prime")
            return "False"
            break
    else:
        print(n,"is prime")
    return "True"