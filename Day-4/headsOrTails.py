import random

usersChoice = input("Choose one - Heads or Tails ?")

random_integer_0_or_1 = random.randint(0,1)

if random_integer_0_or_1==0:
    result = "heads"
else:
    result = "tails"

if usersChoice.lower()==result:
    print(f"Congratulations! Its a {usersChoice}")
else:
    print(f"Alas! You lose, its a {result}")