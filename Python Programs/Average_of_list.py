# Python Program to Find Average of a List

def Average(a):
    sum=0
    count=0
    for i in a:
        count=count+1
        sum=sum+i
        avg=sum//count
    return avg

