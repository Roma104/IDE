###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)

total = dice_roll_1 + dice_roll_2 + dice_roll_3

print(f'Roll one: {dice_roll_1}')
print(f'Roll two: {dice_roll_2}')
print(f'Roll three: {dice_roll_3}')
print(f'Sum of the rolls: {total}')