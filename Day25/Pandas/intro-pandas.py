with open('weather_data.csv') as data_file:
  data = data_file.readlines()
  print(data)

import csv
with open('weather_data.csv') as data_file:
  data = csv.reader(data_file)
  days = []
  temperatures = []
  conditions = []
  for row in data:
    temperatures.append(row[1])
    days.append(row[0])
    conditions.append(row[2]


import pandas

data =  pandas.read_csv("weather_data.csv")
print(type(data) # Pandas DataFrame
print(data)
print(type(data["temp"])) #Pandas Series
