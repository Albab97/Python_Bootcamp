import random
import myModule

random_integer = random.randint(1,10)  # randint(a,b) --> a <= N <= b , (N is integer)
print(random_integer)

print(myModule.my_favourite_number)

random_number_0_to_1 = random.random()  # random() --> 0 <= X < 1, (X is floating point number) 
print(random_number_0_to_1)

random_number_0_to_7 = random.random()*7
print(random_number_0_to_7)

random_float = random.uniform(1,10) # uniform() --> a <= X <= b, (X is floating point number)
print(random_float)