# with open("weather_data.csv", "r") as weather_data:
#     weather_data = weather_data.readlines()

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"]
print(temperatures)
