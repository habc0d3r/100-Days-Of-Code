travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries
def add_new_country(country_name, visit_times, cities_names):
  new_place = {}
  new_place["country"] = country_name
  new_place["visits"] = visit_times
  new_place["cities"] = cities_names
  travel_log.append(new_place)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



