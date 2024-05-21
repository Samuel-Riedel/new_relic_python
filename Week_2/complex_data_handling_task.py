
students = [
    {"name": "John", "grades": [88, 76, 92, 56], "class": "biology"},
    {"name": "Jane", "grades": [80, 80, 84], "class": "chemistry"},
    {"name": "Dave", "grades": [78, 80, 88,21,19], "class": "algebra"}
]

for student in students:
    grades = student["grades"]
    for grade in grades:
        print(f"Grade: {grade}")