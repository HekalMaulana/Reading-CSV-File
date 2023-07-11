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
# Read CSV file
data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"].tolist()

# Get average data
temp_average = sum(temperatures) / len(temperatures)
print(f"{temp_average:.4f}")
print(data.temp.mean())

# Get maximum data
max_data = data["temp"].max()

# Get data in row
print(data[data.temp == data.temp.max()])


