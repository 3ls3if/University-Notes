
students = []

with open("students.csv") as file:
    for line in file:
        name, value = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["value"] = value
        student = {"name": name, "value": value}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name, reverse=False):
    print(f"{student['name']} is a {student['value']}")

# for student in sorted(students, key=lambda student: student["name"], reverse=False):
#     print(f"{student['name']} is a {student['value']}")