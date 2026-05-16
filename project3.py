
#Ticket booking for Roller coaster ride
print("Welcome to RollerCoaster Ride")
height = float(input("Enter your height in cm: "))
bill = 0
if height >= 120:
    print("Hoore! You can ride :)")
    age = int(input("Enter your Age: "))
    if age <= 12:
        bill += 5
        print("Please pay for ride $05")
    elif age >=18 and age <=44 :
        bill += 7
        print("Please pay for ride $07")
    elif age >=45 :
        bill = 0
        print("Enjoy Your Free Ride")
    else:
        print(":)")
    photo = input("Do you want a taken photo for $3 then type 'y' if No then type 'N'")
    if photo == 'y':
        bill += 3
    print(f"Your total amount to pay is ${bill} ")
else:
    print("OOps you can't ride :(" )
