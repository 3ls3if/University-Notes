import re

name = input("What's your name? ").strip()

# if "," in name:
#     last, first = name.split(", ?")
#     name = f"{first} {last}"

# print(f"hello, {name}")

# matches = re.search(r"^(.+), *(.+)$", name)

# if matches:
if matches := re.search(r"^(.+), *(.+)$", name):
    # last, first = matches.groups()
    last = matches.group(1)
    first = matches.group(2)

    name = f"{first} {last}"

print(f"hello, {name}")

