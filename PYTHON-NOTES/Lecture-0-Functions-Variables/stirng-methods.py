
name = input("What is your name: ")

# Remove whitespace from str
name = name.strip()

# Capitalize
name = name.capitalize()

# Title
name = name.title()

# Split user's name into first name and last name
first, last = name.split()

print(f"Hello, {first}")


