# Tells you if you have enough mileage for your trip
# 8 kyu

def zero_fuel(distance_to_pump, mpg, fuel_left):
    fuel = distance_to_pump / mpg
    if fuel > fuel_left:
        return False
    else:
        return True
