#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :17th Feb 2023
# File : table-2.py


# import module
from tabulate import tabulate

# assign data
mydata= [
    ['a' , 'b' , 'c'] ,
    [12,34,56] ,
    ['roses' , 'for' , 'roses!']
]

# display table
print(tabulate(mydata))