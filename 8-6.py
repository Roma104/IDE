###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter how much liters your viacle consums per 100km: '))
total_fuel_consumption = distance * (fuel_consumption/100)
total_cost = total_fuel_consumption * fuel_price
print(f'Your vihacle consumed {total_fuel_consumption} l of fuel.')
print(f'Your have to pay: {total_cost} pln.')