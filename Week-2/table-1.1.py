#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :17th Feb 2023
# File : table-1.1.py

# import module
from tabulate import tabulate

# assign data 
mydata = [
    [ "David" , "Nairobi"] ,
    [ "Reina" , "Maziwa"] ,
    [ "Mashua" , "Roysambu"] ,
    [ "Robert" , "Kisumu"]
]

# create header
head = [ "Name" , "City" ]

# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))