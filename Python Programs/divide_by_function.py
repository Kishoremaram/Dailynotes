#program to find number divisible by 3&4
def divis(n):
    count=0
    for i in range(1,n):
        if i%3==0 and i%4==0:
            count=count+1
    return count

print(divis(50))
    
    
