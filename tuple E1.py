city_info = [
    ("Mumbai","India",21_000_000),    
    ("Tokyo","Japan",41_000_000),
    ("Moscow","Russia",13_000_0000)
    ]


def take_city(city):
    for name,country,population in city:    
        print(f"{name}, {country} — population: {population}")
    
take_city(city_info)