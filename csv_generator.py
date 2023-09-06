import copy
import csv
import random


#INPUT Gabe, 14, Basketball, exam1 80 exam2, ….exam4
#OUTPUT Gabe, 14, bball, exam1, exam2, …exam4, 85.6

#name,age,hobby,Calc11,Calc12,Pre-Calc1,Pre-Calc2,ArtHistory1-> 

#name,age,hobby,Calc11,Calc12,Pre-Calc1,Pre-Calc2,ArtHistory1-> 
#AVG(Calc11,Calc12,Pre-Calc1,Pre-Calc2,ArtHistory1)
"""
N students
M classes
Return average grade per student across classes
"""

HEADERS = [
    "FIRST",
    "LAST",
    "AGE",
    "HOBBY",
    "EXAM_1_GRADE",
    "EXAM_2_GRADE",
    "EXAM_3_GRADE",
    "EXAM_4_GRADE",
    ]

STUDENTS = {
    "Bil Westerfield": {},
    "Bill Edwards": {},
    "David Chen": {},
    "William Chen": {},
    "Rafferty Russell": {},
    "Laura Hunt": {},
    "John Cena": {},
}

HOBBIES = [
    "Basketball",
    "Starcraft",
    "Football",
    "Soccer",
    "Band",
    "Choir",
    "Dance",
    "Photography"
]

CLASSES = [
    "Physics",
    "Chemistry",
    "Calculus",
    "World History",
    "American History",
    "Biology"
    ]

rows = []
# Set demographic info
for student in STUDENTS:
    STUDENTS[student] = {
        "FIRST": student.split(" ")[0],
        "LAST": student.split(" ")[1],
        "AGE": random.randint(14, 17),
        "HOBBY": random.choice(HOBBIES),
    }

    # Set grades
    for class_name in CLASSES:
        STUDENTS[student]["CLASS"] = class_name
        STUDENTS[student]["EXAM_1_GRADE"] = random.randint(0,100)
        STUDENTS[student]["EXAM_2_GRADE"] = random.randint(0,100)
        STUDENTS[student]["EXAM_3_GRADE"] = random.randint(0,100)
        STUDENTS[student]["EXAM_4_GRADE"] = random.randint(0,100)

        rows.append(copy.deepcopy(STUDENTS[student]))

#print(STUDENTS.get("Bill Edwards"))
#print(rows)
# print(len(rows))


with open("student_grades.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys(),delimiter=',', quotechar='"', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)