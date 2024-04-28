
email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")