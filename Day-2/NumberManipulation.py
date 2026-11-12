bmi = 77 / 1.73**2
print(bmi)

# Flooring a number : removing the decimal places and keep only integer part
print(int(bmi))

# Rounding number : Mathematical round off

print(round(bmi))
print(round(bmi,2)) # Round off to 2 decimal places

# Assignment Operator

score = 0
score+=1 # score = score + 1
print(score)
score-=1
print(score)
# Similary score*=1 and score/=1

# f-strings
score = 0
height = 1.73
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")