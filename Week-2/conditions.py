#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :17th Feb 2023
# File : conditions.py

age = 24
gender = "male"

if (age < 18 ):
    print(" You are still young ")
else:
    print("you should get an id")


    #compund / multiple conditions
if (age > 30) & (gender == 'male'):
    print("you qualify for a loan")
else:
    print("no loan for you ")

fav_colour = "grey"
age = 22
if(fav_colour == 'grey') | (age <= 22):
    print("happy birthday to you")
else:
    print("no birthday present yet!")

