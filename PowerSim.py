cities = {
    #   First Town
    "city_1_location_X" : 2,
    "city_1_location_Z" : 6,
    "city_1_demand" : 2.3,   # In MW

    #   Second Town
    "city_2_location_X" : 3,
    "city_2_location_Z" : 8,
    "city_2_demand" : 0.4   # In MW
}

plants = {
    #   Plant 1
    "plant_1_location_x" : 0,
    "plant_1_location_y" : 0,
    "plant_1_capacity" : 1  # In MW
}

if cities["city_1_demand"] + cities["city_2_demand"] > plants["plant_1_capacity"]:
    print("Alert! Too much electricity being used!")
else:
    print("everything is fine!")