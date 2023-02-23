#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :22nd Feb 2023
# File : advanced data_types.py



# advanced data types
#mutable vs immutable
#mutable are data types that can be edited or change during program life cycle
#add/remove elements
#immutable are data types thart cant be edited duriing program life cycle
#1) list(mutable)
#2)tuples(immutable)
#3)dictionaries AKA dict

#dict uses key and value pair
student={"Name":"Bob" ,"age":24 ,"gender":"male","is_tall":True}

print(student["Name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])
print(student.values())
print(student.keys())

#"Name":"Bob" --> name(key) Bob(value)
#4 sets 
#fuctions
#date and time(python module)
#project oriented
#programming
#object and class
#pip
#file handling
#sets is used to store multiple items in a single file it uses curly
#e.g.{"Faith","orange"}
#sets are further into -order
                        #non-order
my_fruits={"orange","apples","kiwi","banana"}
print(my_fruits)

for fruit in my_fruits:
    print(fruit)
    print(type(my_fruits))
    print(len(my_fruits))
    

friends=["mark","annita","faith","yvonne"]
#or friends=[] for empty list
# add --> append(),extend()

students=["marie","kigen","serphine"]

friends.extend(students)
friends.append("bob")
friends.sort()
friends.reverse()
#type of list that are immutable(tuples)

stationeries=("pens","ink","sharpener","stapler")

#you can replace the whole tuple
stationeries=("ruler","clipboard","eraser","rubber")
for stationery in stationeries:
    print(stationery)
    #tuple can allow duplicates
    nmubers=(1,2,3,4,76,98,21)
