students = []

with open("students.csv") as file:
    for line in file:
        name, value = line.rstrip().split(",")
        students.append(f"{name} is a {value}")

for student in sorted(students):
    print(student)