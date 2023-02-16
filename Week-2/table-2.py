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