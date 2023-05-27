for i in range(1000):
    num=i
    temp=num
    l=len(str(num))
    sum=0
    while num>0:
        digit=num%10
        sum=sum+digit**l
        num=num//10
    if temp==sum:
        print(temp)
