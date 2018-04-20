magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # Indented part is inside the for loop:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Non-indented part is outside of the for loop:
print("Thank you, everyone. That was a great magic show!")
