X = int(input("Enter First Side  : "))
Y = int(input("Enter Second Side : ")) 
Z = int(input("Enter Third Side  : "))
S= (X+Y+Z)/2
Area = (S*(S-X)*(S-Y)*(S-Z))**0.5
print("The area of triangle is : ",Area)
