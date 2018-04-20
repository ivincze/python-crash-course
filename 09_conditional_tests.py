# Check equality:
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Boolean values:
car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')

# Case insensitive equals:
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

# Check inequality:
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Check inequality on numbers:
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# Mathematical comparisons:
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

# Logical AND:
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
# same as:
b = (age_0 >= 21) and (age_1 >= 21)
print(b)

# Logical OR:
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# List contains:
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# List doesn't contain:
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
