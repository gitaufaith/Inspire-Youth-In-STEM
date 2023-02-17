#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :16th Feb 2023
# File : table-3.py

from prettytable import PrettyTable

#Specify the Column Names while initializing the Table
myTable = PrettyTable(["Student Name" , "Class" , "Section" , "Percentage"])

#Add rows
myTable.add_row(["Leonara" , "X" , "B" , "90.8%" ])
myTable.add_row(["Penina" , "X" , "C" , "70.4%"  ])
myTable.add_row(["Sasha" , "X" , "A" , "54.9%"   ])
myTable.add_row(["Talia" , "X" ,"D" , "83.2%"    ])
myTable.add_row(["Keren" , "X" ,"A" , "34.8%"     ])

print(myTable)
