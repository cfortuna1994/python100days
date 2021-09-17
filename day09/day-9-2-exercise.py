
travel_log = {
    "France" : {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12 }, 
    "Germany" : {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5},
}



travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12 
    }, 
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]

def add_new_country(Country, visits, cities):
    new_data = {}
    travel_log.append(Country, visits, cities) 


#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)