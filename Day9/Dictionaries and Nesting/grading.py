student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Draco": 74,
    "Akbar": 91,
    "Hanip": 80,
    "Abc": 65
}

# TO DO 1: Create an empty dictionary called student_grades
student_grades = {}

# TO DO 2: Write your code below to add the frades to student_grades.
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80 and score <= 90:
        student_grades[student] = "Exceeds Expectation"
    elif score >70 and score <=80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)