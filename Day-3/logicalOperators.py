# Logical Operators are used to combine multiple conditions. Mainly three logical operators - 'and', 'or' and 'not'.
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("What is your age?"))
    if age < 12:
        print("Pay $5.")
    elif age <= 18: 
        print("Pay $7.")
    elif age>=45 and age<=55:   # Use of Logical Operator 'and'
        print("Pay $0.")
    else:
        print("Pay $12.")
else:
    print("Sorry you have to grow taller before you can ride this.")