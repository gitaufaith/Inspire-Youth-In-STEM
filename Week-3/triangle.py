#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :21st Feb 2023
# File : triangles.py


rows=int(input("Enter the number of rows"))
k=2*rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end="")
        k=k-1
        for j in range(0,i+1):
            print("*",end="")
            print("")
            print("----------------")
            k=rows-2
            for i in range(rows,-1,-1):
                for j in range(k,0,-1):
                    print(end="")
                    k=k+1
                    for j in range(0,i+1):
                        print("*",end="")
                        print("")