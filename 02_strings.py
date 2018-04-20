name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

# Apostrophe
message = "One of Python's strengths is its diverse community."
print(message)

# SyntaxError: invalid syntax:
# message = 'One of Python's strengths is its diverse community.'
# print(message)

name = "Vinnie"
print("Hello " + name + ", would you like to learn some Python today?")

author = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
message = author + ' once said, "' + quote + '"'
print(message)

# Stripping:
name = " \n \t Imre Vincze \t \n "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

age = 40
message = "Happy " + str(age) + "th Birthday!"
print(message)
