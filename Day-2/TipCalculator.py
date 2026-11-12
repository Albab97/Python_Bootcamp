print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill?")


total_bill = float(bill)
tip_percent = int(tip)
number_of_persons = int(people)

actual_tip = tip_percent/100*total_bill

actual_total_bill = total_bill+actual_tip

bill_per_person = round(actual_total_bill/number_of_persons,2)

print(f"Each person should pay: ${bill_per_person}")