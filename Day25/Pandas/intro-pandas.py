# Traditional way of handling data in files
# with open("weather-data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

# Using csv library
# import csv
#
# with open("weather-data.csv") as data_file:
#    data = csv.reader(data_file)
#    print(data)
#    days = []
#    temp = []
#    cond = []
#    for row in data:
#        if row[0] != "Days":
#            days.append(row[0])
#        if row[1] != "Temperature":
#            temp.append(row[1])
#        if row[2] != "Condition":
#            cond.append(row[2])
# print(days)

# Using pandas library
import pandas

data = pandas.read_csv("weather-data.csv")
# print(data)  # pandas DataFrame
# print(data["Temperature"])  # pandas Series

# temp_list = data["Temperature"].to_list()
# avgTemp = sum(temp_list)/len(temp_list)
# print(f"Average of Temperatures is {avgTemp}")
# or you can use Series methods
# print(data["Temperature"].mean())
# print(data["Temperature"].max())
# print(data["Temperature"].min())

# Get data in row with filtering
# print(data[data.Temperature == data.Temperature.max()])
monday = data[data.Days == "Monday"]
print(monday.Temperature)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Maktum", "Shahid", "Hanip"],
    "scores": [78, 77, 77]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("student_data.csv")
