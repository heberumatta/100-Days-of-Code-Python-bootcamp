# with open("02-intermediate/25-Day-Pandas/weather_data.csv") as df:
#     data = df.readlines()
#     print(data)

# import csv

# with open("02-intermediate/25-Day-Pandas/weather_data.csv") as df:
#     data = csv.reader(df)
#     temperatures = []
# 
#     for row in data:
#         temperature = row[1]
#         if temperature != "temp":
#             temperatures.append(temperature)
#     print(temperatures)

import pandas as pd
data = pd.read_csv("02-intermediate/25-Day-Pandas/weather_data.csv")
print(data["temp"])

# If we need to calculate the average of temp
temp_avr = data["temp"].mean()
print(f"\nAverage: {temp_avr}")

# If we need to extract the high value of temp:
temp_high = data["temp"].max()
print(f"max: {temp_high}\n")

print(data["temp"].describe())

# Get Data in Row
# To get an especific row: data-frame[Serie <Condition> <Serie/Value>]
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

# Math
data["temp"] = (data.temp * 9/5) + 32
print(data.temp)

# Create a data-fram from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

# data-frame = df
df = pd.DataFrame(data_dict)
print(df)