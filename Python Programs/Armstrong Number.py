num=int(input("enter number:"))
temp=num
l=len(str(num))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit**l
    num=num//10
if temp==sum:
    print(temp,"is am armstrong number")
else:
    print(temp,"is not armstrong number")


