#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :20th Feb 2023
# File : lists_revisited.py

myFavouriteFruits=["Apple","Pineapple","Banana","Melon","lime"]
for fruit in myFavouriteFruits:
    print(fruit)
    print(len(fruit))

my_favourite_fruits =["Banana","Mango","Melon"]
for fruit in my_favourite_fruits:
    print(len(my_favourite_fruits))

friends=["sasha","talia","zuhura","roberto"]
print(friends) 
friends[0]="daniel"
print(friends)
print("-------------------")

new_friends= friends.copy()
print(new_friends)
new_friends= friends.sort()
print(new_friends)
new_friends=friends.pop()
print(new_friends)

new_friends=friends.reverse()
print(new_friends)


