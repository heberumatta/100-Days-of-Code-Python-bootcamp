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