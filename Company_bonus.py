
Year = int(input("Enter Times Spend in the Company: "))
Salary = float(input("Enter the current salary: "))
if Year>10:
    Bonus=(Salary*10)/100
    Salary=Salary+Bonus
    print("net amount of a employee",Salary)
elif Year>6 and Year<10:
    Bonus=(Salary*8)/100
    Salary=Salary+Bonus
    print("net amount of a employee",Salary)
elif Year<6:
    Bonus=(Salary*5)/100
    Salary=Salary+Bonus
    print("net amount of a employee",Salary)
else:
    print("net amount of a employe ",Salary)

    