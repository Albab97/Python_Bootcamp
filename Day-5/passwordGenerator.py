import random

letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to Py Password Generator")
nr_letters = int(input("How many letters would you like in your password ?\n"))
nr_numbers = int(input("How many numbers would you like in your password ?\n"))
nr_symbols = int(input("How many symbols would you like in your password ?\n"))

password_list = []
for i in range(1,nr_letters+1):
    password_list.append(letters[random.randint(0,len(letters)-1)])
for i in range(1,nr_numbers+1):
    password_list.append(numbers[random.randint(0,len(numbers)-1)])
for i in range(1,nr_symbols+1):
    password_list.append(symbols[random.randint(0,len(symbols)-1)])
print(password_list)

# Easy Level
final_password = ""
for ch in password_list:
    final_password+=ch
print(final_password)

# Hard Level - All jumbled

hard_password = ""
for ch in password_list:
    hard_password+=random.choice(password_list)

print(hard_password)

# can also be done using random.shuffle()

random.shuffle(password_list)
print(password_list)
