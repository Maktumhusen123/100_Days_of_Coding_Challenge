# Dictionary Comprehension
# (pattern are : {new_key:new_value for item in list},
# {new_key:new_value for (key,value) in dict.items()},
# {new_key:new_value for (key,value) in dict.items() if test})
import random
names = ["Maktum", "Shahid", "Akbar", "Hanip", "Abdul"]
student_score = {name: random.randint(1,100) for name in names}
print(student_score)

passed_students = {student: score for (student, score) in student_score.items() if score > 60}
print(passed_students)

