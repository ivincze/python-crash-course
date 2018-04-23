age = 12

if age < 4:
  print("Your admission cost is $0.")
elif age < 18:
  print("Your admission cost is $5.")
else:
  print("Your admission cost is $10.")

if age < 4:
  price = 0
elif age < 18:
  price = 5
elif age < 65:
  price = 10
else:
  price = 5
print("Your admission cost is $" + str(price) + ".")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
  if requested_topping == 'green peppers':
    print("Sorry, we are out of green peppers right now.")
  else:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

requested_toppings = []
# Check if list is empty:
if requested_toppings:
  for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
  print("\nFinished making your pizza!")
else:
  print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print("Adding " + requested_topping + ".")
  else:
    print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
