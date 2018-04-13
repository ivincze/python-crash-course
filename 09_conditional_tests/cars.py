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
