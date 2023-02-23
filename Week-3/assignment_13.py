#simple interest
principal=float(input("enter the principal amount:"))
time=float(input("enter the time taken:"))
rate=float(input("enter the rate:"))

interest=(principal*rate*time)/100
print("simple interest for a given pricipal amount,rate of interest,and time period is :",interest)


#linear motion
def linear_motion(m,x,c):
    y=m*x + c
    return y 

    #quadratic expression
def quadratic_equation(a,x,b,c):
    y=a*(x**2) + b*x + c
    return y 

def add_numbers(num1,num2,num3):
        sum_num=num1+num2+num3
        print(sum_num)

    #calling the function
add_numbers(2,4,6)
quadratic_equation(2,4,7,9)
