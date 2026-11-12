import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    
'''
paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
images = [rock,paper,scissors]

users_input = input("What do you choose ? Type 0 for Rock, 1 for Paper and 2 for Scissors.")
users_choice = int(users_input)
print(images[users_choice])

computer_choice = random.randint(0,2)
print(f"Computer choose {computer_choice}")
print(images[computer_choice])

if((users_choice==0 and computer_choice==2) or (users_choice==1 and computer_choice==0) or (users_choice==2 and computer_choice==1)):
    print("You win")
if ((users_choice==2 and computer_choice==0) or (users_choice==0 and computer_choice==1) or (users_choice==1 and computer_choice==2)):
    print("You lose")
if (users_choice==computer_choice):
    print("Try again")