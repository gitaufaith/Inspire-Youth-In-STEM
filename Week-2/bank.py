#!/usr/bin/python3

# This is a single line comment
# Python program to illustrate the use of operators
# Name :Gitau Faith
# Email : gitaufaith@gmail.com
# Date :17th Feb 2023
# File : bank.py


#write a program that calculates 16% on tax income
#ranging between 100k -500k

#19% tax income if between 150k -300k
#30% tax income if above 300k
#5% tax income if less than 100k

#print gross income ,net income
net_income= input("Enter your net income")

#above 300k
if(net_income >= 300000):
    gross_income = net_income+ ((30/100)* net_income)
    print("since your net income{} your gross income is {}" .format(net_income,int(gross_income)))

    #150k to less than 300k
    if(net_income>= 150000) &  (net_income < 300000):
        gross_income=net_income +((30/100)*net_income)
        print("since your net income is {} your gross income is {}" .format(net_income ,int(gross_income)))

        #100k to less than 150k
        if(net_income>= 100000) & (net_income < 150000):
            if(net_income>=100000) & (net_income < 150000):
                gross_income=net_income + ((16/100)*net_income)
                print("since your net income is {} your gross income is {}" .format(net_income,int(gross_income)))

                #from 1 to less than 100k
                if(net_income>= 1) & (net_income < 100000):
                    gross_income=net_income+((5/100)*net_income)
                    print("since your net income is {} your gross income is {}" .format(net_income,int(gross_income)))

        else:
            print("invalid argument!")

         
