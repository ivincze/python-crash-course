# Range (exclusive stop index):
for value in range(1,5):
    print(value)

# Create list by range:
numbers = list(range(1,6))
print(numbers)

# Skip numbers in a given range:
even_numbers = list(range(2,11,2))
print(even_numbers)
odd_numbers = list(range(1,10,2))
print(odd_numbers)

# Squares:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# List comprehension:
squares = [value**2 for value in range(1,11)]
print(squares)
cubes = [i**3 for i in range(1,11)]
print(cubes)

# Statistics:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
