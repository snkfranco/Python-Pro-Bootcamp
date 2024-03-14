import os

os.system('cls')

size = input('\n What size pizza do you want? S, M, or L   >> ') # What size pizza do you want? S, M, or L
add_pepperoni = input(' Do you want pepperoni? Y or N   >> ') # Do you want pepperoni? Y or N
extra_cheese = input(' Do you want extra cheese? Y or N   >> ') # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

if size == 'S':
  pizzaPrice = 15
  if add_pepperoni == 'Y':
    pizzaPrice += 2
  if extra_cheese == 'Y':
    pizzaPrice += 1

elif size == 'M':
  pizzaPrice = 20
  if add_pepperoni == 'Y':
    pizzaPrice += 3
  if extra_cheese == 'Y':
    pizzaPrice += 1

elif size == 'L':
  pizzaPrice = 25
  if add_pepperoni == 'Y':
    pizzaPrice += 2
  if extra_cheese == 'Y':
    pizzaPrice += 1

print("\n\n Thank you for choosing Python Pizza Deliveries!")
print(f' Your final bill is: ${pizzaPrice}.')