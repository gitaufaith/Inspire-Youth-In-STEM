#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :21st Feb 2023
# File : diamond.py

a=int(input("Enter number:"))

y=a -1
for i in range(1,a+1):
    space=" " *y
    stars="* " *i
    print(space+stars)
    y=y-1


y=a -1
for i in range(1,a+1):
    space=" " *i
    stars="* " *y
    print(space+stars)
    y=y-1

    #print


