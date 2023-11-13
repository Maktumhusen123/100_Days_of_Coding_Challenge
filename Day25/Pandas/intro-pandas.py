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
print(data)  # pandas DataFrame
print(data["Temperature"])  # pandas Series
