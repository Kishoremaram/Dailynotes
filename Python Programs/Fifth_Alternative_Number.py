#program to print 5th element of list
def alter(n):
    list1=[]
    for i in range(1,n):
        list1.append(i)
    print("list:",list1)
    list2=[]
    for j in range(5,len(list1),5):
        list2.append(j)
#print("alternate list:",list2)
    return list2
        
