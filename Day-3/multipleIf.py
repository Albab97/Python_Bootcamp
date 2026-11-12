height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child ticket : $5.")
    elif age <= 18:
        bill = 7 
        print("Youth ticket : $7.")
    else:
        bill = 12
        print("Adult ticket : $12.")
    want_photos = input("Do you want a photo ? Type y for Yes and n for No.")
    if want_photos == "y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride this.")