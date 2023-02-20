net_income=int(input("what is your net income"))
gross_income=int(input("what is your gross income"))
tax_group_a=(gross_income* 0.05)
tax_group_b=(gross_income*0.16)
tax_group_c=(gross_income*0.19)
tax_group_d=(gross_income*0.30)

if gross_income < 100000:
    print("gross income:",gross_income)
    print("tax =",tax_group_a)
    print("net_income",gross_income - tax_group_a)
elif(gross_income > 190000) & (gross_income < 150000):
    print("gross_income:",gross_income)
    print("tax =",tax_group_b)
    print("net_income:",gross_income - tax_group_b)
elif(gross_income>= 1500000)& (gross_income<= 300000):
    print("gross_income",gross_income)
    print("tax =",tax_group_c)
    print("net_income:",gross_income - tax_group_c)

else:
    print("gross_income",gross_income)
    print("tax =",tax_group_d)
    print("net_income:", gross_income - tax_group_d)
