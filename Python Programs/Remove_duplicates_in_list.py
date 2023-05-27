# Python Program to Remove Duplicates from a List
def dupli(list1):
    new_list=[]
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    return(new_list)
