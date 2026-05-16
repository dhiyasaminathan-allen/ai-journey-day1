print("Hello");
name="Sandhiya";
print("Hello I am " + name);
print("Day 1: Complete");
print("Day 2: Starting");


#Calculate BMI value
print("BMI Claculator")
height = float(input("Enter your Height: "))
weight = float(input("Enter your Weight: "))
bmi = height / weight
print("Your BMI value is: ",bmi)





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
    elif 18 <= age <= 44:
        bill += 7
        print("Please pay for ride $07")
    elif 45 <= age <= 55:
        bill = 0
        print("Enjoy Your Free Ride")
    else:
        print("You can't ride at this age --safety first-- :)")
    photo = input("Do you want a taken photo for $3 then type 'y' if No then type 'N'")
    if photo == 'y':
        bill += 3
    print(f"Your total amount to pay is ${bill} ")
else:
    print("OOps you can't ride :(" )

