city_1 = {
    #   First Town
    "location_X" : 2,
    "location_Z" : 6,
    "demand" : 0.4   # In MW
}

city_2 = {
    #   Second Town
    "location_X" : 3,
    "location_Z" : 8,
    "demand" : 0.4   # In MW
}

plant_1 = {
    #   Plant 1
    "location_x" : 0,
    "location_y" : 0,
    "capacity" : 1,  # In MW
}

plant_2 = {
    #   Plant 2
    "location_x" : 10,
    "location_y" : 5,
    "capacity" : 1  # In MW
}

cityList = [city_1, city_2]
plantList = [plant_1, plant_2]

if plant_1["capacity"] - city_1["demand"] <= 0:
    print("Warning Not Enough Power For City 1")
else:
    print("Everything Is Fine For City 1")