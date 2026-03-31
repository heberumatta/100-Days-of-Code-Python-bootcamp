country = {
    "Argentina": {"Capital": "Buenos Aires", "Provincias": ["Corrientes", "Cordoba", "Neuquen"]},
    "Paraguay" : {"Capital": "Asuncion", "Provincias": ["Encarnacion","Punta del Este"]}
}

print(country["Argentina"]["Capital"])
print(country["Paraguay"]["Provincias"])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

#Figure out how to print out "Stuttgart" from the following list:

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])
