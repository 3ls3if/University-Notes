
import csv

students = []

with open("students2.csv") as file:
    reader = csv.reader(file) 
    for name, value in reader:
        students.append({"name": name, "value": value})

for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is a {student['value']}")