#Password Generator
letters = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#","$","%","^","&","*","(",")"]

print("Create you Own password in just seconds :)")

ps_letters = int(input("Enter how many letters you want: "))
ps_numbers = int(input("Enter how many numbers you want: "))
ps_symbols = int(input("Enter how many symbols you want: "))

password = [ ]
for choose in range(0, ps_letters):
    password += random.choice(letters)

for choose in range(0, ps_numbers):
    password += random.choice(numbers)

for choose in range(0, ps_symbols):
    password += random.choice(symbols)


random.shuffle(password)



full_password = " "
for choice in password:
    full_password += choice

print(f"Your Generated Password is: {full_password}")
