###
# A program that calculates the distance to the horizon from a height given in meters from the keyboard. 
#Then, using the program, calculate the distance to the horizon in km when:
#
#i.You are standing on a beach, by the sea, on the water line 
#(calculate the distance for your height in m). You have probably been to the seaside many times. 
#Can you believe that the horizon is only a few kilometers away?
##
#ii.You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.
#
import math

hight_in_meters = input('Enter the hight you are on in meters: ')
hight_in_meters = int(hight_in_meters)

hight_in_km = hight_in_meters/1000

distance_to_the_horizon = round(3.57 * math.sqrt(hight_in_km), 2)

print('Your distance to the horizon is: ', distance_to_the_horizon, "km")