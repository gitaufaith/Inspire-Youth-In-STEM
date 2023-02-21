#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :9th Feb 2023
# File : variables.py

n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
        for j in range(2*i+1):
            print("*" ,end="")
        print() 

