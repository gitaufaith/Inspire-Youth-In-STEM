#write a program that calculates arithmetic progression from 1 to 20
#formula n=nth term in the sequence,a=first term,d=common difference
#AP=a+(n-1)d
nth_term=20
first_term=1
common_difference=input("what is the common difference:(should be<9>)")
if (int(common_difference)> 9):
    print("out of range!!!")
else:
    arithmetic_progression=first_term +((nth_term -1) +int(common_difference))
    print("The arithmetic progression is:",arithmetic_progression)
