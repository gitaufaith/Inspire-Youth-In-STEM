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

