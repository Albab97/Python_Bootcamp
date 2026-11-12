print(int("1234")) # int() method converts the object inside parenthesis to an integer.
print(int("123")+int("456"))

# We have to be careful while converting datatypes into one another. For ex - below statement would throw ValidError

# print(int('abc')) # ValueError

print(float(3))
print(str(321))
print(bool(341))
print(bool(0))

print("Number of letters in your name: "+ str(len(input("Enter your name")))) # If str() method is not there for type conversion "TypeError" will appear
