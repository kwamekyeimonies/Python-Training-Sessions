friends = {
    "Tenkorang",
    "Daniel",
    "Kwame",
    
}

country={
    "Ghana",
    "Dubai",
    "London",
    "USA"
}

next_country={
    "Ghana",
    "Amsterdam",
    "Cuba",
    "Usa",
    "Canada"    
}

country_difference = country.difference(next_country)
next_country_diff = next_country.difference(country)
print(country_difference)
print(next_country_diff)
print("Set union",country.union(next_country))
print("Set Intersection", country.intersection(next_country))

