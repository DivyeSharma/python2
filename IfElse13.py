height_limit = 105
age_limit = 8

height = int(input("Enter your height "))
age = int(input("Enter your age "))
if height >= height_limit:
    if age >= age_limit:
        print("You may go to the ride ")
    else:
        print("Your are too young for this ride. Sorry ")
else:
    print("You can not go on this ride. You are too short. Sorry ")