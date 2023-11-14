import pandas
student_dict = {
    "students": ["Maktum", "Shahid", "Akbar"],
    "scores": [60, 58, 55]
}
# Looping through Dictionaries
'''for (key, value) in student_dict:
    print(key)
    print(value)'''

student_data = pandas.DataFrame(student_dict)

for (key, value) in student_data.items():
    print(key)
    print(value)

for (index, row) in student_data.iterrows():
    print(row)
    print(row.students)

