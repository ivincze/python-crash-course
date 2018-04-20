# Tuples are immutable lists:
dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

# Looping through tuple:
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Rewriting tuple (no mutation):
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
