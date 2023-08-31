# Nesting a list in a dictionary

travel_log = {
    "India" : ["Karnataka", "Kerala", "Andra Pradesh", "Tamilnadu"],
    "France" : ["Paris", "Lille", "Dijon"],
}

# Nesting a Dictionary in Dictionary
travel_log = {
    "India" : {
        "cities_visited": ["Karnatka", "Kerala", "Andra Pradesh", "Tamilnadu"],
        "visits": [10, 5, 4, 2]
    },
    "France" : {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "visits": [1, 2, 3]
    }
}

# Nesting a Dictionary in List
travel_log = [
    {
        "country": "India", 
        "cities_visited": ["Karnatka", "Kerala", "Andra Pradesh", "Tamilnadu"]
    },
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"]
    }
]

