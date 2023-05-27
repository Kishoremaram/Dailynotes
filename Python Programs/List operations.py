///list1 = [1,5,8,10,15]
///print("List before reversed:",list1)
///list2=[]
///for value in list1:
///    list2=[value]+list2
///print("List after reverse:",list2)

list1=[]
for i in range(1,101):
    list1.append(i)
print("list:",list1)
list2=[]
for j in range(5,len(list1),5):
    list2.append(j)
print("alternate list:",list2)