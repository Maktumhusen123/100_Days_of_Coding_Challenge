travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "India",
        "visits": 32,
        "cities": ["Karnataka", "TamilNadu", "Kerala"]
    }
]
# TO DO: Write the function that will allow new country to be added to the travel_log
def add_new_country(country_name, num_visits, cities_names):
    travel_log.append({"country":country_name,"visits":num_visits,"cities":cities_names})


add_new_country("Russia", 2, ["Moscow"])
print(travel_log)