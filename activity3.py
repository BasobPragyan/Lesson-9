print("Select your ride : ")
print("1.Bike")
print("2.Car")
choice_1=int(input("Enter choice : "))
if (choice_1==1):
    print("What type of bike : ")
    print("1.Scopty/n")
    print("2.Motorbike/n")
if (choice_1==1):
    print("You have selected scoooty")
else:
    print("You have selected Motorbike")
choice_2=int(input("Enter choice : "))
if (choice_2==2):
    print("What type of car : ")
    print("1.Sedan")
    print("2.SUV")
    print("3.Luxury")
if(choice_2==1):
    print("You have selected a sedan")
    if(choice_2==2):
        print("You have selected SUV")
        if(choice_2==3):
            print("You have selected Luxury")
else:
    print("Wrong Choice")