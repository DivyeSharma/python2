Driving_Age = 16
Smoking_Age = 18
Lotto_Age = 19
Drinking_Age = 21

Age = int(input("How old are you "))
if Age > Drinking_Age:
    print("You can drive, smoke, gamble, and drink! woohoo! ")
elif Age > Lotto_Age:
    print("You can drive, smoke, and gamble! yipeee! ")
elif Age > Smoking_Age:
    print("You can drive and smoke! Nice ")
elif Age > Driving_Age:
    print("You can drive! Vroom Vroom ")
else:
    print("You can`t even drive")
