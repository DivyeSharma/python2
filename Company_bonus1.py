current_year = int(input("Enter your current year: "))
join_year = int(input("Enter the year of joining: "))
diff = current_year - join_year
if diff > 3:
    print("Bonus of Rs : 2500 /- ")
else:
    print("No Bonus")