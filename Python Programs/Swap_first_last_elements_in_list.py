# Python Program to Swap the First and Last Element in a List
def swapping(l):
    temp=l[0]
    l[0]=l[-1]
    l[-1]=temp
    #l[0],l[-1]=l[-1],l[0]
    return(l)
