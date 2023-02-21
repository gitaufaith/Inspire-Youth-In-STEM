#!/usr/bin/python3
# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :20th Feb 2023
# File : assignment_11.py


#list elelments of favourite musicians
#add 3 new musicians
#create an empty list of favourite musicians
#using for loop add 5 musicians
#copy the to a new list called celebs
#sort the list then pop out 2 celebs and count the remaining celebs in the list
myFavouriteMusicians=[]
myFavouriteMusicians=["celine dion","poppy","snapp"]
for musician in myFavouriteMusicians:
    print(musician)

celebs=[]
celebs=["travis","kylie" ,"chris brown","rose muhando","mr.nice","mr.bean"]
celebs_additional="snoop Dog","loise kim","plankton","meghan trainor","zuchu"
for celeb in celebs_additional:
    print(len(celebs))
    celebs.append(celebs_additional)
    print(celebs)
    print("----------")
new_celebs=celebs.copy()
print(new_celebs)


new_celebs=celebs.pop(0)
print(new_celebs)
new_celebs=celebs.pop(1)
print(new_celebs)



new_celebs= celebs.count(celebs_additional)
print(new_celebs)

new_celebs=celebs.sort()
print(new_celebs)


