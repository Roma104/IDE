####
#Write a program that rolls dice
#then check weather it landed on 1 or 6 
#

import random

dice_roll = random.randint(1,6)

special = dice_roll == 1 or dice_roll == 6

print(f'Your number: {dice_roll}')
print(f'Special roll: {special}')
