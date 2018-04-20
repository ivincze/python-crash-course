# Sort permanently:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sort permanently in reverse order:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sort temporarily:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the reverse sorted list:")
print(sorted(cars, reverse=True))
print("Here is the original list again:")
print(cars)

# Reverse:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Length:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
