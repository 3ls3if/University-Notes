import re

url = input("URL: ").strip()

# print(url)

# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")

# print(f"Username: {username}")

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) 

# print(f"Username: {username}")

# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")