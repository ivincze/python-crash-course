players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Slice (exclusive stop index):
print(players[0:3])
print(players[1:4])

# Slice from the beginning of the list:
print(players[:4])

# Slice through the end of the list:
print(players[2:])

# Slice by indexing from end of the list:
print(players[-3:])

# Looping through a slice:
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copy entire list as slice:
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are: " + str(my_foods))
print("My friend's favorite foods are: " + str(friend_foods))

# It doesn't work without [:], it's not a copy but only reference:
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are: " + str(my_foods))
print("My friend's favorite foods are: " + str(friend_foods))
