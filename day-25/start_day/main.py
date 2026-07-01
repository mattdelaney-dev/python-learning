from pathlib import Path

file_path = Path(__file__).parent / "2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv"

# with open(file_path) as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open(file_path) as data_file:
#     data = csv.reader(data_file)
#     temp_list = []
#     for row in data:
#         if row[1] != "temp":
#             temp_list.append(int(row[1]))
#     print(temp_list)

import pandas

# data = pandas.read_csv(file_path)
# # print(type(data))
# # print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# get data in row
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(f"Fahrenheit is {(monday.temp * 2) + 30}")

# create dataframe from stratch
# data_dict = {
#     "students": ["Amy", "James"],
#     "scores": [76, 56]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#How many black, gray and cinnamon squirls from Primary Fur Color

# fur_colours = pandas.read_csv(file_path)
# counts = fur_colours["Primary Fur Color"].value_counts()

# data_dict = {
#     "Fur Color": ["Gray", "Black", "Cinnamon"],
#     "Count": [
#         counts.get("Gray", 0),
#         counts.get("Black", 0),
#         counts.get("Cinnamon", 0)
#     ]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")