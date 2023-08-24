# loops are used to repeat a block of code
# for loop
name_list = ["Maktum","Hanip","Akbar","Shahid","Ullas","Furqan"]

# iterate over list
for name in name_list:
    print(name)

# Average Height Exercise
heights_list = input("Input a list of student heights : ").split()
#print(heights_list)

number_of_students = 0
for i in range(0, len(heights_list)):
    heights_list[i] = int(heights_list[i])
    number_of_students += 1
#print(heights_list)

total_height = 0
for height in heights_list:
    total_height += height
print(f"Sum of all heights: {total_height}")

average_height = total_height // number_of_students
print(f"Average Height : {average_height}")