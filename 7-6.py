###
# Vehicle can drive in speed between 40 and 140 km/h
# Print True whether a car is riding with good speed or False otherwise.
#
car_speed = int(input('Enter car speed in km/h: '))
is_speed = car_speed >= 40 and car_speed <= 140
print(f'Car is from Krakow: {is_speed}')