
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students3.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

    print("Data written successfully!")

# The code above writes data to a CSV file. What is the name of the file?