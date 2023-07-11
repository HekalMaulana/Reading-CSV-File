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
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# temperatures = data["temp"].tolist()

# Get average data
# temp_average = sum(temperatures) / len(temperatures)
# print(f"{temp_average:.4f}")
# print(data.temp.mean())

# Get maximum data
# max_data = data["temp"].max()

# Get data in row
# print(data[data.temp == data.temp.max()])

# Get Monday temp and change his temp to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# fahrenheit = (1.8 * monday_temp) + 32
# print(fahrenheit)

# Create data from scratch
# data_dict = {
#     "students": ["Hekal", "Zaki", "Iqbal"],
#     "scores": [70, 80, 90],
# }
#
# data_student = pandas.DataFrame(data_dict)
# print(data_student)

fur_color_grey = (data['Primary Fur Color'] == 'Gray').sum()
fur_color_red = (data['Primary Fur Color'] == 'Cinnamon').sum()
fur_color_black = (data['Primary Fur Color'] == 'Black').sum()

squirrel_count = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [fur_color_grey, fur_color_red, fur_color_black],
}

squirrel_data = pandas.DataFrame(squirrel_count)
squirrel_data.to_csv("squirrel_count.csv")
