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