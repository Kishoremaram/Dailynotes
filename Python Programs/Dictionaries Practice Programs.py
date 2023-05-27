# car ={"brand": "Ford","model": "Mustang","year": 1964}
# print(car.get("brand"))

# if you want to update
# car["year"]= 2020
# print(car)

# if you want to add a key,value pair

# car["colour"]="red"
# print(car)

#if you want to clear the values

# car.clear()
# print(car)

#if you want to delete the values

# del car["brand"]
# print(car)

#nested dictionary

# people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
#           2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}

# print(people[1]["name"],people[2]["lastname"])

#add a record to nested dictionary

# people[1]["hight in feets"]= 6
# people[2]["hight in feets"]= 5
# print(people)

# people[3]={'name': 'tendulkar', 'age': '45', 'profession': 'Ex cricketer',"lastname":"sachin"}
# people[3]
# print(people)

# delete a record from nested dict

# del people[3]["lastname"]
# print(people)

# delete a   nested dict from dict
# del people[3]
# print(people)


# copying from one dictionary to another

# yourdict = {"brand": "Ford","model": "Mustang","year": 1964}
# mydict = yourdict.copy()
# print(mydict)


# Example2

yourdict = {"brand": "Ford","model": "Mustang","year": 1964}
# mydict = dict(yourdict)
# print(mydict)
# print(yourdict.keys())


# checking key is there or not
# if "model" in yourdict.keys():
# print("Yes, 'model' is one of the keys in the  dictionary")
#
#
# if "Ford" in yourdict.values():
#   print("Yes, 'Ford' is one of the value in the  dictionary")


# loop through dictionary
# mydict={'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"}
# mydict["role"]="student"
# print(mydict)
#getting only values

# for x in mydict.values():
#     print(x)

#getting only keys

# for x in mydict.keys():
#     print(x)

#getting  keys with values

# for x,y in mydict.items():
#     print(x,y)



#
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
#
# print(myfamily)

# dict1={'sun':71,'mon':72,'tue':65,'wed':74}
# print(dict1)
# dict1['sun']=61
# dict1['mon']=81
# dict1['tue']=101
# dict1['wed']=121
# print(dict1)

# students={'john':20,'ria':21,'ann':22}
# # students.setdefault('john')
# # print(students)
# # students.setdefault('anabel')
# # print(students)
# # students.setdefault('roo',10)
# # print(students)

# numbers = {1:"one",2:"two",3:"three"}
# print(numbers)

# capital_city={"nepal":"kathmandu","england":"london"}
# # print("Intial Dictionary:",capital_city)
#
# capital_city["japan"]="tokyo"
# print(capital_city)
# capital_city["japan"]="tokyo"
# print(capital_city)
#
# del capital_city
# print(len(capital_city))
# print(sorted(capital_city))
# clear(capital_city)
# print(values(capital_city))

# dict1 = {"A": "hello","B": "world"}
# dict2 = {"B": "good morning"}
# dict1.update(dict2)
# print(dict1)

# dict1 = {"x":"Hai"}
# dict2 = ["y","Great"]
# dict1.update({"y":"I'm","z":"fine"})
# dict1.update(y="where",z="somewhere")
# dict1.update([dict2])
# dict1.update([("a","hello"),("b","there")])
# print(dict1)

# dict1 = {"City":"Hyderabad","State":"Telangana"}
# dict1["City"] = "Warangal"
# print(dict1)

# dict1 = {1: "one", 2: "two", 3: "three"}
# dict2 = {}
# for key, value in dict1.items():
#     dict2[key] = value
# print(dict2)

# dict1={1:"one",2:"two",3:"three"}
# dict2=copy.copy(dict1)
# print(dict1)
# dict2[3]="None"
# print(dict1)

# dict1 = {1:"one",2:[1,2,3],3:"three"}
# dict2 = dict1.copy()
# dict2[2][0] = "888"
# print(dict1)
# print(dict2)

# import copy
#
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.deepcopy(old_list)
#
# old_list[1][1] = 'AA'

# print("Old list:", old_list)
# print("New list:", new_list)

# dict1={1:"one",2:"two",3:"three"}
# dict2=dict(dict1)
# print(dict2)


# dict1 = {10: 'a', 20: [1, 2, 3], 30: 'c'}
# dict2 = dict1.copy()  # copying using copy() method
# # Updating dict2 elements and checking the change in dict1
# dict2[10] = 10
# dict2[20][2] = '45'  # list item updated
# print("Updated copy:", dict2)
# print("Given Dictionary:", dict1)

# import copy
#
# # given dictionary
# dict1 = {10: 'a', 20: [1, 2, 3], 30: 'c'}
# # new dictionary
# dict2 = copy.deepcopy(dict1)  # copying using deepcopy() method
# # Updating dict2 elements and checking the change in dict1
# dict2[10] = 10
# dict2[20][2] = '45'  # list item updated
# print("Updated copy:", dict2)
# print("Given Dictionary:", dict1)

# dict1={1:"one",2:"two",3:"three"}
# del dict1[2]
# dict1.pop(1)
# dict1 = {key:value for key,value in dict1.items() if key!=2}
# print(dict1)

# d = {
#     "fantasy": "harrypotter",
#     "romance": "me before you",
#     "fiction": "divergent"
# }
# for i in d.items():
#     print(i)
# print(d.items())

# d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
# for i in sorted(d.values()):
#     print(d[i],end=" ")

### remove no value items from Dictionary
# mutidict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}


# fruitsDict = {'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
# fruitsDict2 = {'mango': 120,'guava': 30}
# fruitsDict.update(fruitsDict2)
# print(fruitsDict)


# people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
#           2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
# del people[2]
# # print(people)
# people[3]={"A":"Sachin","B":"Dravid","C":"Shewag"}
# print(people)
