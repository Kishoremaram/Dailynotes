#program for palindrome

# str1=input("Enter string: ")
#
# def palindrome(str1):
#     rev=""
#     for i in str1:
#         rev=i+rev
#     if str1==rev:
#         print("palindrome")
#     else:
#         print("not palindrome")
#
# palindrome(str1)

# num = int(input("enter the number:"))
# k = 0
# while (num > 0):
#     digit = num%10
#     k = k*10+digit
#     num = num//10
# print(k)

# str1=input("Enter string: ")
# def palindrome(str1):
#     count = 0
#     j=-1
#     for x in range(len(str1)):
#         if str1[x] == str1[j]:
#             count = count+1
#             j=j-1
#     if count==len(str1):
#         print("This is palindrome")
#     else:
#         print("This is not palindrome")
# palindrome(str1)

# dict1={1:'A',"2":'B',"3":'C'}
# i=input("enter key:")k
# if i.isdigit():
#     k = int(i)
#     if (k in dict1) or (i in dict1):
#         print("key is present")
#     else:
#         print("key not present")

# s="python  is,,pgmlang.."
# for i in s:
#     str1 = s.replace("  ",":")
#     str2 = str1.replace(",,",":")
#     str3 = str2.replace("..",":")
# print(str3)


# Write a python program to right rotate a List by n
# Enter position to rotate list item: 3
# Sample input: [10, 20, 30, 40, 50, 60, 70]
# Expected output: [50, 60, 70, 10, 20, 30, 40]

# list1 = [10, 20, 30, 40, 50, 60, 70]
# list2 = []
# n=int(input("Enter position to rotate:"))
# for i in range(len(list1)):
#     if i>n:
#         list2.append(list1[i])
# for j in range(len(list1)):
#     if j<=n:
#         list2.append(list1[j])
# print(list2)

# l=[10, 20, 30, 40, 50, 60, 70]
# k=int(input("enter the number to rotate: "))
# x=l[k+1:]+l[0:k+1]
# print(x)

# Write a program to multiply two given number without using “*” operation and any in built function


a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
total=0
for i in b:
    total = total+a
print(total)
