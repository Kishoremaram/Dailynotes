#program to reverse of list
def reverse(list1):
    print("List before reversed:",list1)
    list2=[]
    for value in list1:
        list2=[value]+list2
    print("List after reverse:",list2)
    return list2
