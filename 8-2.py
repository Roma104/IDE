###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

import math

pi = round(math.pi,2)

r = int(input("Enter r: "))

pole = pi * r**2

obwod =2 * pi * r

print(f'Pole wynosi: {pole}; Obwód wynosi: {obwod}. Pi: {pi}')