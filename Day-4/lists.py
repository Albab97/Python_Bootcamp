states_of_america = ["Delaware","Pennsylvania","Texas","Florida","Kansas","Hawai","Alaska"]

print(states_of_america)

states_of_america[1]="Maine"
states_of_america[2]="Vermont"

print(states_of_america)

states_of_america.append("California")
print(states_of_america)

states_of_america.extend(["Washington DC","Michigan"])

print(states_of_america)

states_of_america.remove("Washington DC")
print(states_of_america)

# Nested List

dirty_dozen = ["Spinach","Kale", "Collard", "Mustard Greens","Strawberries","Grapes","Nectarines","Peaches","Cherries","Apples","Blackberries","Pears","Potatoes","Blueberries"]

dirty_dozen_fruits = ["Strawberries","Grapes","Nectarines","Peaches","Cherries","Apples","Blackberries","Pears","Blueberries"]

dirty_dozen_vegetables = ["Spinach","Kale","Collard","Mustard Greens","Potatoes"]

dirty_dozen_nested = [dirty_dozen_fruits,dirty_dozen_vegetables]

print(dirty_dozen_nested)