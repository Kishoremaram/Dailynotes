#Program to check lists are same or not
list1=[1,2,3,2,1]
list2=[1,3,2,2,1]
list1.sort()
list2.sort()
if list1 == list2:
    print("lists are equal")
else:
    print("list are not equal")
