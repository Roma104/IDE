###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
feet = cm // 30.48
feet_remainder = cm % 30.48
inches = cm // 2.54
inches_remainder = cm % 2.54
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
#print(f'feet remainder: {feet_remainder}, inches remainder: {inches_remainder}.')